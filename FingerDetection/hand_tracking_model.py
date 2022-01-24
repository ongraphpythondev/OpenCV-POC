# we are going to use MediaPipe(developed by google)
from unittest import result
import cv2 as cv
import mediapipe as mp
import time 

cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
# choose default parameter for Hands method
hands = mphands.Hands()
# for drwaing dots and connection of our hand in cam or image
mpdraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while True :
    success , frame = cap.read()
    imgRGB = cv.cvtColor(frame , cv.COLOR_BGR2RGB)
    results = hands.process(frame)
    # print(results.multi_hand_landmarks)
    # there are total of 21 points for hand tracking or detection
    # which is found for only one hand
    # for more no. of hand it will increase.
    if results.multi_hand_landmarks :
        for handLms in results.multi_hand_landmarks :
            for id,lm in enumerate(handLms.landmark):
                print(id,lm)
                h,w,ch = frame.shape  
                cx , cy = int(lm.x*w) , int(lm.y*h)
                print(id ,cx,cy)
                
                if id == 0 :
                    cv.circle(frame , (cx,cy) , 15 , (255,0,255) , cv.FILLED)
                if id == 4:
                    cv.circle(frame, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                if id == 8:
                    cv.circle(frame, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                if id == 12:
                    cv.circle(frame, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                if id == 16:
                    cv.circle(frame, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                if id == 20:
                    cv.circle(frame, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                
            # its drawing dot/points of detected hand
            # mpdraw.draw_landmarks(frame ,handLms)
            
            # drawing dot with its connect for detected hand
            mpdraw.draw_landmarks(frame, handLms , mphands.HAND_CONNECTIONS)
            
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(frame , f'{int(fps)}',(10,70) , cv.FONT_HERSHEY_PLAIN , 3 ,
               (255,0,255) , thickness=3)
    
    cv.imshow("Image" , frame)
    cv.waitKey(1)