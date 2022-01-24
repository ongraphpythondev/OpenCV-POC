import os
from charset_normalizer import detect
import cv2 as cv
import time

from matplotlib.pyplot import draw 
import HandTrackingModule as htm

def FrameScaling(frame , wscale=0.5 , hscale=0.5):
    width = int(frame.shape[1]*wscale)
    height = int(frame.shape[0]*hscale)
    dimension = (width,height)
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

wCam ,hCam = 648 , 488

cap = cv.VideoCapture(0)
cap.set(3 , wCam) #setting width of cam
cap.set(4, hCam) #setting height of cam

folderPath = "finger_images"
myList = os.listdir(folderPath)
print(myList)

overlayList = []

for imPath in myList:
    image = FrameScaling(cv.imread(f'{folderPath}/{imPath}') , 0.09 ,0.09)
    image = image[image.shape[0]//2:image.shape[0],image.shape[1]//2-200:image.shape[1]]
    # print(image.shape)
    # cv.imshow(f'{imPath}',image)
    overlayList.append(image)
    

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)
tipIds = [4,8,12,16,20]

while True :
    success , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img , draw=False)
    # print(lmList)
    cv.putText(img, "Press key 'z' for exit",
               (10, 450), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    
    if len(lmList) != 0:
        fingers = []
        
        # Thumb 
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 Fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)
        cv.putText(img , f'Count : {totalFingers}' ,
                   (10,70) ,cv.FONT_HERSHEY_PLAIN,2,(0,255,0) ,thickness=3)
    
        h, w, ch = overlayList[totalFingers-1].shape
        # img[0:h, 0:w] = overlayList[totalFingers-1]
        cv.rectangle(img , (5,40),(200,80) , (0,255,0),2)    
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv.putText(img , f"FPS : {int(fps)} ",(470,70),cv.FONT_HERSHEY_PLAIN ,2,(255,0,0),thickness=3)
    cv.rectangle(img, (465, 40), (630, 80), (255, 0, 0), 2)
    
    
    cv.imshow('Image',img)
    # press key 'z' for exit
    if cv.waitKey(1) & 0xFF == ord('z') :
        break


