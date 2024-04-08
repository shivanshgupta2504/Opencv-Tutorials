import cv2 as cv

img = cv.imread('cow-salt-peper.png')

noise_removed_img = cv.medianBlur(img, 5)

cv.imshow('Normal Img', img)
cv.imshow('Noise removed img', noise_removed_img)

cv.waitKey(0)