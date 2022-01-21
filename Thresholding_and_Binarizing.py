
import cv2 as cv

'''
Thresholding :
Thresholding is the binary realization of an image , 
In general , we want to take an image and convert it to
a binary image that is an image where pixels are either
0 or black and 255 or white.
EXAMPLE : 
Take an image and take some particular value that we're
going to call the thresholding value And 
Compare each pixel of image to this threshold of value.
If that pixel intentsity is less than the threshold value,
we set that pixel intensity to zero or black And If it is 
above this threshold value , we set it to 255 or white.
so in this sense ,  we can esstentially create a binary image
just froma regular standalone image.

There are mainly 2 types of thresholding :
1> Simple Thresholding
2> Adaptive Thresholding
'''

def FrameScaling(frame , scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width , height)
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)


img = FrameScaling(cv.imread('Photos/city1.jpg'),0.10)
cv.imshow('City',img)

# grascale image
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale",gray)

# Simple Thresholding
# cv.threshold(src_img , threshold_value , max_value , threshold_type , dst(default=None))
# threshold_value <max_value

'''
cv.threshold() returns two values 
1> thresh : it is binarized image of src image
2> threshold : it is essentially same value that you passed (in this its 150)
'''
threshold , thresh = cv.threshold(gray , 150 ,255 , cv.THRESH_BINARY)
cv.imshow('Simple Thresholded',thresh) 

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

'''
Disadvantage of simple thresholding is that we have to provide
thresholding value manually ,it might work on some cases but
for advance visioning it will not work .
'''

# Adaptive Thresholding
'''
In this we gonna let computer find the optimal threshold value 
by itself And using that value that refines , it binarizes over
the image .
so, thats an essence that entire crux of adaptive thresholding.
cv,adaptivethreshold(src_img , max_value , adaptive_method,
threshold_type , blocksize , C , dst(default is None))
'''

adaptive_thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow('Adaptive Thresholding' , adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 13, 3)
cv.imshow('Adaptive Mean Thresholding Inverse', adaptive_thresh_inv)

# gaussian put weight on each pixel value and calculate mean of it
adaptive_thresh_inv = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 13, 3)

cv.imshow('Adaptive Gaussian Thresholding Inverse', adaptive_thresh_inv)

cv.waitKey(0)