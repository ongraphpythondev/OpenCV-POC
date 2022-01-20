import cv2 as cv
import numpy as np

def scalingFrame(frame , scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width , height)
    return cv.resize(frame ,dimension , interpolation=cv.INTER_AREA)

img = cv.imread('Photos/dog3.jpg')
img = scalingFrame(img , 0.1)
cv.imshow("Dog1",img)

# Translation
'''
Using translation, we can shift images up ,down ,left and right.
'''
# x and y is for number of shift to shift.
def translation(img , x, y):
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img , transMatrix , dimensions)

# -x -> left
# -y -> Up
# x -> right
# y -> Down

translated = translation(img , 100,100)
# cv.imshow('Translated',translated)


# Rotation
def rotate(img , angle , rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None :
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint , angle , 1.0)
    dimensions = (width , height)
    
    return cv.warpAffine(img , rotMat , dimensions)

# anti clock-wise
# rotated = rotate(img , 45)
# cv.imshow('Rotated1',rotated)
# clock-wise
rotated = rotate(img, -45)
# cv.imshow('Rotated2', rotated)

rotated = rotate(rotated, -90)
# cv.imshow('Rotated2', rotated)


# Resizing image
resized = cv.resize(img , (500,500) , interpolation=cv.INTER_CUBIC)
# cv.imshow('Resizing',resized)


# fliping image
'''
flip method have 3 flip code:
0 -> vertically
1 ->horixontally
-1 ->both vertically and horizontally
'''
# vertically
flip = cv.flip(img ,0)
# cv.imshow('Flip1',flip)

# horizontally
flip = cv.flip(img ,1)
# cv.imshow('Flip2',flip)

# Both vertically an horizontally
flip = cv.flip(img, -1)
# cv.imshow('Flip3', flip)

# Cropping image
crop = img[30:300,140:380]
cv.imshow('Cropped',crop)



cv.waitKey(0)