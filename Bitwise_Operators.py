import cv2 as cv
import numpy as np


blank = np.zeros((400,400), dtype='uint8')
rect = cv.rectangle(blank.copy() , (30,30) , (370,370), 255 , -1)

circle = cv.circle(blank.copy() , (200,200),200,255,-1)


cv.imshow('rectangle' , rect)
cv.imshow('Circle',circle)

# Bitwise AND returns intesecting regions

AND = cv.bitwise_and(rect , circle)
cv.imshow('Bitwise AND',AND)

# Bitwise OR returns both intersecting and non-intersecting regions
OR = cv.bitwise_or(rect,circle)
cv.imshow('Bitwise OR',OR)

# Bitwise NOT return all region in which polygon or figgure is not there

NOT = cv.bitwise_not(rect)
cv.imshow('Bitwise NOT',NOT)

# Bitwise XOR returns non-intesecting regions
XOR = cv.bitwise_xor(rect , circle)
cv.imshow('Bitwise XOR',XOR)



cv.waitKey(0)