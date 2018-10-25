from keras.models import load_model
import cv2
import numpy as np


new_model = load_model('Dogs_vs_cats_model.h5')

#Her kan vi se at det faktisk stemmer overens med modellen vår.
new_model.summary()
new_model.get_weights()
new_model.optimizer()

model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=1e-4), metrics=['acc'])


img = cv2.imread('animals/test/1.jpg')
img = cv2.resize(img,(224,224))
img = np.reshape(img,[1,224,222444,3])

prediction = model.predict_classes(img)

print prediction
