import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

harr_cascade = cv.CascadeClassifier("harr_face.xml")

while True :
    isTrue , frame = capture.read()
    
    print(isTrue)
    
    gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    
    cv.imshow('GrayScale' , gray)
    
    faces_rect = harr_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=4)
    
    for (x,y,w,h) in faces_rect :
        cv.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , thickness=2)
        cv.putText(frame , "FACE" , (x , y-5) , cv.FONT_HERSHEY_SIMPLEX , 1.0 , (255,255,255) , thickness=2)
    
    cv.imshow("Video Cam",frame)
        
    if cv.waitKey(25) & 0xFF == ord('d'):
        break

capture.relese()
cv.destroyAllWindows()
    