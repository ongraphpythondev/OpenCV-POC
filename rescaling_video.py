import cv2 as cv

def changeRes(width , height):
    #Only for Live Video
    capture.set(3,width)
    capture.set(4,height)
    
    
    


def rescaleFrame(frame , scale=0.50):
    #this method will work for Images , Videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimension = (width , height)
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue , frame = capture.read()
    
    frame_resize = rescaleFrame(frame , .2)
    
    cv.imshow("Video Resized" , frame_resize)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


