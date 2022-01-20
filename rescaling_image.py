import cv2 as cv


def rescaleFrame(frame , scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width , height)

    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)


img = cv.imread('Photos/dog3.jpg')

cv.imshow("Dog1", img)

rescaled_img = rescaleFrame(img , 0.15)

cv.imshow("DOG1 rescaled",rescaled_img)

cv.waitKey(0)
