from cProfile import label
import os
import cv2 as cv
import numpy as np

people = ['Chris Evans', 'Chris Hemsworth', 'Mark Ruffalo','Robert Drowney Jr', 'Scarlett Johansson']
DIR = r'C:\Users\india\Desktop\OpenCv\FaceRecognition\faces\train'
haar_cascade = cv.CascadeClassifier("harr_face.xml")

'''
p = []
for i in os.listdir(DIR):
    p.append(i)
print(p)
'''
features = []
labels = []

# looping train 


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        print(path)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
f = len(features)
l = len(labels)
# print(f'length of featues = {f}')
# print(f'length of labels = {l}')

print('Training Done ................')

# converting to numpy array
features = np.array(features , dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features and labels lists

face_recognizer.train(features , labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)