import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Photos/dog.jpg')

blank = np.zeros(img.shape[:2] , np.uint8)
cv.imshow("Blank",blank)


mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

# Color Histogram
colors = ('b', 'g', 'r')

plt.figure()
# plt.title('GrayScale Histogram')
plt.title('Color Histogram')
plt.xlabel('Bins')  # represent no. of intervals in pixel intensities
plt.ylabel('# of pixels')
print(masked.shape)

# note : don't use masked image for masking instead use that circle or 
# any other shape that you used for masking that image.
for i, col in enumerate(colors):
    # hist = cv.calcHist([img], [i], None, [256], [0, 256])
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])


plt.show()



cv.waitKey(0)