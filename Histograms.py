# Computing Histograms in OpenCV
'''
Histograms in OpenCV allows us to vistualize pixel intesities
in an image.So,Whether its a Color image or grayscale image
we can vistualize these pixel intensities.
'''
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from pygame import mask


img = cv.imread('Photos/dog.jpg')
cv.imshow('Cat Image',img)

blank = np.zeros(img.shape[:2] , np.uint8)
cv.imshow('Blank',blank)

# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow('GrayScale Image',gray)

mask = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2) ,100,255,-1)
# cv.imshow('Circle',mask)


masked = cv.bitwise_and(img , img , mask=mask)
cv.imshow('Masked',masked)

# GrayScale histogram
# without mask
# gray_hist = cv.calcHist([gray] , [0] , None , [256] , [0,256])

# provding mask
# gray_hist=cv.calcHist([gray], [0], mask_gray, [256], [0, 256])

# plotting histogram using matplotlib
'''
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins') #represent no. of intervals in pixel intensities
plt.ylabel('# of pixels')

plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
''' 

# Color Histogram
colors = ('b','g','r')

plt.figure()
# plt.title('GrayScale Histogram')
plt.title('Color Histogram')
plt.xlabel('Bins')  # represent no. of intervals in pixel intensities
plt.ylabel('# of pixels')
print(masked.shape)

for i , col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist , color=col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)
