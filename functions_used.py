import cv2 as cv

def scaleFrame(frame,scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width , height)
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)
    

img = cv.imread('Photos/dogs1.jpg')
img = scaleFrame(img , 0.1)
cv.imshow('BGR Cat' , img)

# >>> Converting image to grayscale
# BGR -> GrayScale
# image of cat will be black and white means in gray

# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Cat' , gray)


# Blur image
# cv.GaussianBlur(image_variable , kernal_Size , borderType)
blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
blur1 = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
'''
cv.imshow('Blur Image',blur)
'''
# cv.imshow('Blur Image2',blur1)

# Edge Cascade
'''
Edge Cascade means trying to find edges in the image.
and those shows those edges in new window.
'''

canny = cv.Canny(blur1 , 125, 175)
# cv.imshow('Canny Edges', canny)


# Dilating the images

dilated = cv.dilate(canny , (7,7) , iterations=3)
# cv.imshow("Dilated",dilated)


# Eroding
erode = cv.erode(dilated, (7, 7), iterations=3)
# cv.imshow('Erode ',erode)

# resizing image

# this might sigly effect image
resized = cv.resize(img, (500, 500))
# cv.imshow('Resized1', resized)

# this will resize image without effecting it
resized = cv.resize(img , (500,500) , interpolation=cv.INTER_AREA)
# cv.imshow('Resized2',resized)


# this will resize image into much larger dimension (see both)
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
# cv.imshow('Resized3', resized)

# inter_cubic is slowest but image is much higher quality than any other.
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized4', resized)

# Cropping image
'''
We know that an image is an Array so for cropping image we just 
have to do array slicing 

'''
cropped = img[50:400,200:400]
cv.imshow("Cropped",cropped)






cv.waitKey(0)