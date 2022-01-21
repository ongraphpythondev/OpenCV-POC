from tkinter import Frame
import cv2 as cv
import numpy as np
# Gradient (Edge Detection)
# from programming prospective gradient and edges 
# might seem same but in any other view they are different.

def FrameScaling(frame, h_scale=0.5 , w_scale=0.5):
    width = int(frame.shape[1]*w_scale)
    height = int(frame.shape[0]*h_scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = FrameScaling(cv.imread('Photos/italy.jpg'),0.15,0.2)
cv.imshow('Italy',img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale',gray)

# Similliar as Canny edge detector

# Laplacian
# in this black white pixel interchanges as well.
# we convert all pixel value of image to absolute values.
# then , we convert it into image spectific datatype
lap = cv.Laplacian(gray , cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacian',lap)


# Sobel Gradient magnitude Representation
'''
Sobel computes the gradient in two directions ,the x and y ,
cv.sobel(img_src , ddepth , x-axis , y-axis , dst(None as default))
there are more parameters than metioned above.
Sobel computes gradient(edges) in x and y direction.
and byb combining both of them x and y sobel we get 
a better detailed gradient of image.
'''
# for x axis
sobelx = cv.Sobel(gray , cv.CV_64F , 1 , 0)

# for y axis
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx , sobely)


# cv.imshow('Sobel X' , sobelx)
# cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny Edge Detector
'''
Canny is the advance dege detection algorithm which also make 
use of sobel in one of its stages for edge detection.
'''
canny = cv.Canny(gray , 150 , 175)
cv.imshow('Canny' , canny)


cv.waitKey(0)