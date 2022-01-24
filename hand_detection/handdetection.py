import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
hand = cv.CascadeClassifier('haar_cascades\haar_hand.xml')
palm = cv.CascadeClassifier('haar_cascades\haar_palm.xml')
fist = cv.CascadeClassifier('haar_cascades\haar_fist.xml')
while True :
    isTrue , frame = cam.read()
    
    gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    
    hand_rect = hand.detectMultiScale(gray , 1.1 , 3)
    palm_rect = palm.detectMultiScale(gray, 1.1, 3)
    fist_rect = fist.detectMultiScale(gray, 1.1, 3)
    
    for (x,y,w,h) in hand_rect:
        cv.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,100) , thickness=2)
        cv.putText(frame , 'Hand' ,(20,20), cv.FONT_HERSHEY_COMPLEX , 1.1 , (150,150,0) , thickness=2)
    for (x, y, w, h) in palm_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (100, 255,0), thickness=2)
        cv.putText(frame, 'Palm', (frame.shape[1]-100, 20), cv.FONT_HERSHEY_COMPLEX,
                   1.1, (150, 150, 200), thickness=2)
    for (x, y, w, h) in fist_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (200, 255, 50), thickness=2)
        cv.putText(frame, 'Fist', (20 , frame.shape[0]-100), cv.FONT_HERSHEY_COMPLEX,
                   1.1, (150, 150, 150), thickness=2)

    
    cv.imshow("Cam Detect",frame)
    
    if cv.waitKey(25) & 0xFF == ord('z') :
        break

cam.release()
cv.destroyAllWindows()
