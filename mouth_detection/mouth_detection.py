import cv2 as cv

cam = cv.VideoCapture(0)
eye_cascade = cv.CascadeClassifier('haar_cascades\haar_mouth.xml')


while True:
    isTrue, frame = cam.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    mouth_rect = eye_cascade.detectMultiScale(gray, 2, 3)
    
    if len(mouth_rect) == 0:
        cv.putText(frame, "No mouth detected", (20,20),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), thickness=2)
    
    for (x, y, w, h) in mouth_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255,0 , 0), thickness=2)
        cv.putText(frame, "Mouth Detected", (x, y-5),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), thickness=2)

    cv.imshow("Camera Mouth Detection", frame)

    if cv.waitKey(25) & 0xFF == ord('d'):
        break

cam.release()
cv.destroyAllWindows()
