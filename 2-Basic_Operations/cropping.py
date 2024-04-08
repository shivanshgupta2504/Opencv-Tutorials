import cv2 as cv

img = cv.imread('Sample_Image.png')

print(img.shape) # (1080, 1920, 3)

cropped_img = img[360:720, 640:1280]

print(cropped_img.shape)

cv.imshow('Img', img)
cv.imshow('Cropped_img', cropped_img)

cv.waitKey(0)