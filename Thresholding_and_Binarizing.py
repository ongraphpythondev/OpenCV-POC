import cv2 as cv


img = cv.imread('Photos/dog.jpg')
cv.imshow('Dog',img)

cv.waitKey(0)