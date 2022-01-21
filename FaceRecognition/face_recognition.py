import numpy as np
import cv2 as cv


def FrameScaling(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


haar_cascade = cv.CascadeClassifier('harr_face.xml')

people = ['Chris Evans', 'Chris Hemsworth', 'Mark Ruffalo',
          'Robert Drowney Jr', 'Scarlett Johansson']

features = np.load('features.npy' , allow_pickle=True)
labels = np.load('labels.npy' , allow_pickle=True)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(
    r'C:\Users\india\Desktop\OpenCv\FaceRecognition\faces\val\Scarlett Johansson\wp5202694-black-widow-scarlett-johansson-2020-wallpapers.jpg')

img = FrameScaling(img , 0.4)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

cv.imshow('Person',gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray , 1.1, 4)

for (x,y,w,h) in faces_rect :
    faces_roi = gray[y:y+h , x:x+w]
    
    label , confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img , str(people[label]) , (20,20) , cv.FONT_HERSHEY_COMPLEX , 1.0 , (0,255,0), thickness=2)
    
    cv.rectangle(img , (x,y) , (x+w ,y+h) , (0,255,0) , thickness=2)


cv.imshow("Detected Face",img)

cv.waitKey(0)
    







