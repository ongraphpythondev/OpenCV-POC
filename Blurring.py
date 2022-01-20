from statistics import median
import cv2 as cv


def FrameScaling(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# Blurring Methods
'''
kernalsize is the number of row or column of windows(array element)
in the image pixel.
'''
img = FrameScaling(cv.imread('Photos/pineapple.jpg'),0.1)
img = img[50:img.shape[0]-100,:] #cropping

cv.imshow('PineApple',img)

# Method 1 : Averaging
'''
IN this we set an average pixel intensity by taking average 
of neighbouring pixel boxes intensities
'''
average = cv.blur(img , (3,3)) #kernalsize = 1to7
cv.imshow('Average Blur',average)

# Method 2: Gaussian Blur
'''
It does same thing as averaging except that instead of computing
the average of all of this running pixel ,each running pixel 
is given a particular weight and essentially the average of the
prducts of those weights gives you value of true center.
By using this method, we teds to get less blurry image.
and Gaussian Blur is more natural than averaging Blur.
'''
gauss = cv.GaussianBlur(img , (3,3) , 0)
cv.imshow('Gaussian Blur', gauss)

# Method 3 : Median Blur
'''
this find median instead of mean and work like average blur.
t tends to reduce substential amount of noise.
it is quite good in removing sound and peper noise in image 
as compared to average and Gaussian blur
'''
median = cv.medianBlur(img , 3)
cv.imshow("Median Blur",median)

# Method 4 : Bilateral
'''
Bilateral blurring is most effective and sometimes used in 
a lot of advance computer vision projects , essentially because
of how it blurs.
traditional blurring method just blurred image without looking
at whether you are reducing edges in image or not.
Bilateral blurring applies blurring but retains the eges in the
image.So,you have blurred image but you get to retian the edges
as well.
'''
bilateral = cv.bilateralFilter(img , 10, 35,25)
cv.imshow('Bilateral Blur',bilateral)


cv.waitKey(0)