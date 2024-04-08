import cv2 as cv

img = cv.imread('bear.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# global threshold
ret, thresh = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY)

# for background distinction
# first we'll blur the image
thresh = cv.blur(thresh, (10, 10))
bl = cv.blur(img_gray, (10, 10))

# now we'll again do thresholding
ret, thresh = cv.threshold(thresh, 80, 255, cv.THRESH_BINARY)
ret1, thresh1 = cv.threshold(bl, 80, 255, cv.THRESH_BINARY)

cv.imshow('Main img', img)
cv.imshow('Threshold0 img', thresh)
cv.imshow('Threshold1 img', thresh1)
cv.waitKey(0)