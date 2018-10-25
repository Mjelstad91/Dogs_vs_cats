import os.path
import shutil

"""
ANIMAL_NAMES = ['dog', 'cat']
os.mkdir('animals')
os.mkdir(os.path.join('animals', 'train'))
os.mkdir(os.path.join('animals', 'val'))


##Creating the subfolders for each label
for i in range(len(ANIMAL_NAMES)):
    os.mkdir(os.path.join('animals', 'train', ANIMAL_NAMES[i]))
    os.mkdir(os.path.join('animals', 'val', ANIMAL_NAMES[i]))

#Destination for the dogs :-)
dstDog = "./animals/train/dog"
dstCat = "./animals/train/cat"
#source
src = "./jpg/train"

#Move cats and dogs to their specific folder
for files in os.listdir("jpg/train"):
    print(files)
    if files.startswith("dog"):
        shutil.move(os.path.join(src, files), os.path.join(dstDog, files))
    elif files.startswith("cat"):
        shutil.move(os.path.join(src, files), os.path.join(dstCat, files))

srcVal = "./jpg/val"
dst ="./animals/val"
#Move all the val-data to the val-folder
import shutil
import os
"""
#sourcedir = os.path.join()
#source_list = os.listdir("./animals/train")
cat_destination = "./animals/val/cat"
dog_destination = "./animals/val/dog"
source = "./animals/train"
#cat_source = "./animals/train/cat"
#dog_source = "./animals/train/dog"

i = 0
j = 0
for root, dirs, files in os.walk(source):
   for file in files:
       if file.startswith("cat"):
           if i%5 == 0:
               shutil.move(os.path.join(root, file), os.path.join(cat_destination, file))
               i += 1
           else:
               i += 1
       elif file.startswith("dog"):
           if j%5 == 0:
               shutil.move(os.path.join(root, file), os.path.join(dog_destination, file))
               j += 1
           else:
               j += 1
