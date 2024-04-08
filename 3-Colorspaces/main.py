import cv2 as cv

img = cv.imread('parrot.png')

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imwrite('parrot_rgb.png', img_rgb)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('parrot_gray.png', img_gray)
# in gray scale, only one channel img
# meaning every pixel will have only one channel
# 0 --> complete black, 255 --> complete white

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imwrite('parrot_hsv.png', img_hsv)

cv.imshow('img', img)
cv.imshow('img_rgb', img_rgb)
cv.imshow('img_gray', img_gray)
cv.imshow('img_hsv', img_hsv)
cv.waitKey(0)