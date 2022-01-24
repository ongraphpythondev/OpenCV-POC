import cv2 as cv
import mediapipe as mp 
import time 
import HandTrackingModule as htm

pTime = 0
cTime = 0

cap = cv.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame,draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(frame, f'{int(fps)}', (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), thickness=3)

    cv.imshow("Image", frame)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
