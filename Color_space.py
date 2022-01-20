import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def FrameScaling(frame , scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

#TOPIC :  Color Space
'''
OpenCv reads image in BRG format i.e.., Blue,Green and Red.
But outside of OpenCv , we use RGB format(Red ,Green and Blue format)
which is inverse of OPenCV format.
'''

# BGR Scale
img = FrameScaling(cv.imread('Photos/city3.jpg'),0.2)
cv.imshow("City" , img)

# here matplotlib's pyplot show this BGR image to RGB
# plt.imshow(img)
# plt.show()

# Gray Scale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow("GrayScale",gray)

# BGR format -> HSV(Hue Saturation Value) format
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# BGR -> LAB (L*a*b)
# it tuned into an image into how human preceive color.
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB2', lab)

# BGR -> RGB
rgb = cv.cvtColor(img ,cv.COLOR_BGR2RGB)
# cv.imshow("RGB",rgb)

# plt.imshow(rgb)
# plt.show()

# Converting to BGR
# HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow("HSV To BGR",hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab , cv.COLOR_LAB2BGR)
cv.imshow('LAB TO BGR',lab_bgr)

'''
we cannot convert grayscale to HSV directly , we have to convert
them into BGR first then other grayscale or HSV.
'''

 


cv.waitKey(0)