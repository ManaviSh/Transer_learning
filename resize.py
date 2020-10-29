import cv2
import glob
import os

train_cats = r'E:\Code\Manavi\Projects\project\animal_dataset\train_set\cats' 
train_dogs = r'E:\Code\Manavi\Projects\project\animal_dataset\train_set\dogs'
train_panda = r'E:\Code\Manavi\Projects\project\animal_dataset\train_set\panda'
test_cats = r'E:\Code\Manavi\Projects\project\animal_dataset\test_set\cats'
test_dogs = r'E:\Code\Manavi\Projects\project\animal_dataset\test_set\dogs'
test_panda = r'E:\Code\Manavi\Projects\project\animal_dataset\test_set\panda'

folders = [train_cats, train_dogs, train_panda, test_cats, test_dogs, test_panda]

width = 100# keep original width
height = 100
dim = (width, height)
i=0
for img in glob.glob(test_dogs + '\*.jpg'):
    image = cv2.imread(img)
    print('Original Dimensions : ',image.shape)

    # resize image
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(r'E:\Code\Manavi\Projects\project\resized\test\dogs\image%04i.jpg' %i, resized)
    i +=1
    cv2.imshow('image', resized)
    cv2.waitKey(30)
cv2.destroyAllWindows()



