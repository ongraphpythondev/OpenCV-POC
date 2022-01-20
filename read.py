import cv2 as cv

# READING IMAGES
'''
# below used for reading image.
img = cv.imread('Photos/cat.jpg')
# this show image readed by variable 'img'
cv.imshow('Cat' , img)
#wait for key to be pressed then image window will close
cv.waitKey(0) 
'''

# READING VIDEOS

''' 
We know that video are moving images and that image we call
as frames , these frame moves at certain speed which give us
exprience like things are moving and all image(frame) are related
to each other in a video. 
'''
''''
# below method takes integer argument like 0,1,2,3 ,etc or path of videos.
# here : 
# 0 = webcam of computer or laptop.
# 1 = 1st cam connected to system.
# 2 = 2nd cam connected to system.
# capture = cv.VideoCapture(0)

# we are giving video path.
capture = cv.VideoCapture('Videos/animation.mp4')

# video is being display frame by frame
while True :
    isTrue , frame = capture.read()
    # this frame is like a image 
    cv.imshow('Video' , frame)
    
    # this says if letter 'd' is pressed then break out of the loop. 
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
'''

