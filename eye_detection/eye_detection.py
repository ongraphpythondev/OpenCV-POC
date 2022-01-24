import cv2 as cv

cam = cv.VideoCapture(0)
eye_cascade = cv.CascadeClassifier('haar_cascades\haar_eye.xml')


while True :
    isTrue , frame = cam.read()
    
    gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    
    eye_rect = eye_cascade.detectMultiScale(gray , 1.1 , 5)
    
    for (x,y,w,h) in eye_rect:
        cv.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , thickness=2)
        cv.putText(frame , "Eye Detected" , (x,y-5) , cv.FONT_HERSHEY_COMPLEX , 1.0 , (255,255,255) , thickness=2)
    
    cv.imshow("Camera Eye Detection",frame)
    
    if cv.waitKey(25) & 0xFF == ord('d'):
        break

cam.release()
cv.destroyAllWindows()
        
