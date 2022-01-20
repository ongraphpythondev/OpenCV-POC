import cv2 as cv
import numpy as np

def FrameScaling(frame , scale=0.5 ):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width , height)
    return cv.resize(frame , dimension, interpolation=cv.INTER_AREA)

img = FrameScaling(cv.imread('Photos/dogs1.jpg') , 0.1)
cv.imshow("Sample Image",img)

# Masking
'''
Masking allows us to focus certain part of image that we did 
like to focus.
like : if you have an image of people in it and if you're 
interested in focusing on the faces of people im image .
then you ca essentially aplly masking and mask over people faces 
and remove all unwanted parts of image.
'''

blank = np.zeros(img.shape[:2] , dtype='uint8')
cv.imshow('Blank Image',blank)

# Circle
circle = cv.circle(blank.copy(), ((img.shape[1]//2), img.shape[0]//2) , 100, (255,255,255), -1)
cv.imshow('Mask',circle)

# Rectangle
rect = cv.rectangle(blank.copy(), ((
    img.shape[1]//2)-90, (img.shape[0]//2)-90), ((img.shape[1]//2)+90, (img.shape[0]//2)+190) ,(255,255,255) ,-1 )
cv.imshow('Rectangle',rect)
mask = cv.bitwise_or(rect , circle)
cv.imshow('Weird Shape',mask)

masked = cv.bitwise_and(img ,img, mask=mask)
cv.imshow('Maked',masked)







cv.waitKey(0)
    