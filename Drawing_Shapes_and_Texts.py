import cv2 as cv
import numpy as np

# creating blank image
'''
> here (500,500,3) = (height,width,number_of_color_channel)
> uint8 is date type for image.
'''
blank = np.zeros((500, 500 , 3),dtype='uint8') 
# cv.imshow('Blank Image' , blank)

# 1.> Painting the image a certain color
'''
# green 
blank[:] = (0,255,0)
cv.imshow('Green' , blank)

# Blue
blank[:] = (255, 0, 0)
cv.imshow('Red', blank)

# Red
blank[:] = (0,0,255)
cv.imshow('Blue', blank)

'''

# Painting a portion of image

# blank[200:300,300:400] = (255, 0, 0)
# cv.imshow('Blue', blank)

# 2.> Draw a rectangle
'''
# Blank Rectangle
cv.rectangle(blank , (0,0) , (250,500) , (0,255,0) , thickness=2)

# Filled rectangle
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
# or
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
'''
# drawing by using shape function .
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2 , blank.shape[0]//2), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangle' , blank)


# 3.> Draw a Circle

# cv.circle(image_varible , coordinates , radius , color , thickness) 
# blank circle
# cv.circle(blank , (250,250) , 40 , (0,0,255) , thickness=3)
# works same as above
# cv.circle(blank, (blank.shape[1]//2,
#           blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
# filled circle

# cv.circle(blank, (blank.shape[1]//2,
#           blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)

# cv.imshow("Circle Image" , blank)

# 4.> Draw a line
'''
# line(image_varible , initialCoordinate , finalCoordinate , color , thickness)
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2),  (255,255,255), thickness=3)
cv.line(blank, (100,250),(300,400),  (255, 255, 255), thickness=3)
cv.imshow('Line' , blank)
'''


# 5.> Writing text
'''
putText(image_variable , text , origin , fontsize , color , thickness)
'''
cv.putText(blank , 'Hello, my name is Himanshu!!!' , (0,255) , cv.FONT_HERSHEY_TRIPLEX , 0.9 , (0,255,0) ,2)
cv.imshow('Text' , blank)

cv.waitKey(0)

