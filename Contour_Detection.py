'''
# lines : 
Lines are an element of design and so add to the composition
of an image.
->They direct view's eye into and along a photo to the focal 
point.
->They also impact the mood of a photo, depending on the type
of line and how it is used.

# Edge : 
Edge In Image Processing : Edge can be defined as a set of contigouous 
pixel positions where an abrupt change of intensity(gray or color) value
occurs.
->Edge represent boundaries between objects and background.
->Sometimes the edge-pixel-sequence maybe broken due to insufficient
intensity difference.

# Contour : 
Contour are basically boundary of the objects,the line or 
curve that joins the continuous points along the boundary
of an object.
->Contour joins points of equal elevation(height) above a given
level.
->Contour is a boundary around something that has well defined 
edges, which means that the machine is able to calculate difference
in gradient(significant difference in magnitude of pixel value.)

->Contour are not same as edges but too much similar that sometimes said same.
->Contour are useful tools when you get into shape analysis and
object detection and recognition.
'''
import cv2 as cv
import numpy as np

def scalingFrame(frame , scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width , height)
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)


img = cv.imread('Photos/dogs1.jpg')
img = scalingFrame(img , 0.1)
cv.imshow('Dog' , img)

print(img.shape)
print(img.shape[1], img.shape[0])
blank = np.zeros(img.shape , dtype='uint8')
cv.imshow('Blank',blank)


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur = cv.GaussianBlur(gray , (5,5) , cv.BORDER_DEFAULT)
# cv.imshow('Blurring Image',blur)

# Method 1 :-
# canny edge detector used to find edge cascade in the image.
canny = cv.Canny(img , 125 , 175)
cv.imshow('Canny Edges',canny)

# instead of blurring and Using Canny Edge Detector 

# Method 2 :-
# we can use 'Threshold' (it is easy to use so much preferred.)
# it looks and tries to binaries that image means creates binary format of that image.
ret , thresh = cv.threshold(gray , 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

# last method after doing any of methods :-
# now using findContour method
# cv.CHAIN_APPROX_NONE : returns all the contours in image
# cv.CHAIN_APPROX_SIMPLE : returns only two point or coordinate 

contours , heirarchies = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!') 


cv.drawContours(blank , contours , -1 , (0,0,255) , 1)
cv.imshow("Contours Drawn" , blank)
cv.waitKey(0)

