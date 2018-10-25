import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from keras.models import model_from_json


from keras.applications.vgg19 import decode_predictions, preprocess_input, VGG19
from keras.engine import Model
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

np.random.seed(1234)

train_generator = ImageDataGenerator(preprocessing_function=preprocess_input,
    horizontal_flip=True,
    zoom_range=.2,
    rotation_range=30,
)
train_batches = train_generator.flow_from_directory('animals/train', target_size=(224, 224))

val_generator = ImageDataGenerator(preprocessing_function=preprocess_input)
val_batches = val_generator.flow_from_directory('animals/val', target_size=(224, 224))


indices = train_batches.class_indices
labels = [None] * 2
for key in tqdm(indices):
    labels[indices[key]] = key

pretrained = VGG19(include_top=False, input_shape=(224, 224, 3), weights='imagenet', pooling='max')

for layer in pretrained.layers:
    layer.trainable = False

inputs = pretrained.input
outputs = pretrained.output

print(inputs)
print(outputs)

hidden = Dense(128, activation='relu')(outputs)
dropout = Dropout(.3)(hidden)
preds = Dense(2, activation='softmax')(dropout)

model = Model(inputs, preds)
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=1e-4), metrics=['acc'])

model.fit_generator(train_batches, epochs=50, validation_data=val_batches, steps_per_epoch=1105//4, validation_steps=255//4)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("Dogs_vs_cats_model.h5")
print("Saved model to disk")

model.summary()
