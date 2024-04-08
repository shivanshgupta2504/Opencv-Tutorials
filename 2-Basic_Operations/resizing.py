import cv2 as cv

img = cv.imread('Sample_Image.png')

resized_img = cv.resize(img, (560, 540))  # (width, height)

print(img.shape)  # (1080, 1920, 3) ---> (height, width, channel)
print(resized_img.shape)
cv.imshow('Image', img)
cv.imshow('Resized Image', resized_img)
cv.waitKey(0)
