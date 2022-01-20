import cv2 as cv
import numpy as np


def FrameScaling(frame,scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# Spliting and merging color channels
'''
IN OPenCv , we normally use 3 color channels BGR(Blur ,Green anad Red)

'''
img = FrameScaling(cv.imread('Photos/town2.jpg'),0.1)
cv.imshow('TOWN',img)

blank = np.zeros(img.shape[:2] , dtype=np.uint8)
# blank[:] = 255,255,255 #white
cv.imshow('Blank',blank)


# In this split for that specific color that region in image is whiter.
# like for blue , for all blue color in image will turn too white else black or gray.
# Note : result image is grayscale image with 1 and 0 
# 1 for white and 0 for black 
# but its total 255 shades between black and white.

b ,g ,r = cv.split(img)
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red', r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
# r = cv.merge([b,r,g])
cv.imshow('Merged Image',merged)
# cv.imshow('Random Channel Merging',r)


# now showing actual color by their channel
blue = cv.merge([b , blank , blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('BLue Channel',blue)
cv.imshow('Green Channel', green)
cv.imshow('Red Channel', red)









cv.waitKey(0)