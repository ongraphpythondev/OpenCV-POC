import cv2 as cv

# face Detection
'''
Face Detection is simple recognizing any faces present in the
image.
face detection is performed using classifiers.
A classifier is essentially an algorithm that decide whether
image is positive or negative, whether a face is present or
not.
Now, classifier need to be trained on 1000s and 10s of 1000s
of images with and without faces. But fortunately OpenCV comes
with a lot of pre trained classifiers.
So two main classifers exist today are : 
1> Harr Classifer/Cascade
2> Local binary pattern
'''

# Harr Cascade
'''
it is used for face detection .
In face Detection, it does not involve skin tone or colors
that are present in the image. these harr cascade essentially
look at an object in an image and using the edges tries to
determine whether it's a face or not.
So, we don't need color in our image And we can go ahead and convert
that into grayscale.
'''


def FrameScaling(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


img = FrameScaling(cv.imread('Photos/group3.jpg'),0.2)
cv.imshow('Peoples Image',img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("grayScale",gray)

# C: \Users\india\Desktop\OpenCv\FaceDetection\harr_face.xml

harr_cascade = cv.CascadeClassifier("FaceDetection\harr_face.xml")

# this return rectangular coordinate of faces
faces_rect = harr_cascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=3)
l = len(faces_rect)
print(f'Number of faces found = {l}')

for (x,y,w,h) in faces_rect :
    cv.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , thickness=2)
    
cv.imshow('Detected Faces',img)


'''
This Harr Cascade is much sesitive to noise so, it detect 
and recognize as a face anything show shows a little facial
property by edge.
so, its not used in more advance computer vision
-> Dealings face recognizer is more effective and less sentitive
than Harr Cascade.
'''

cv.waitKey(0)




