import cv2 as cv

img = cv.imread('fruits.jpg')

k_size = 11 # must be an odd number
img_blur = cv.blur(img, (k_size, k_size)) # classic blur
img_guassian_blur = cv.GaussianBlur(img, (k_size, k_size), 3) # Gaussian Blur
img_median_blur = cv.medianBlur(img, k_size) # Median Blur

cv.imshow('Fruits', img)
cv.imshow('Fruits_Blurred', img_blur)
cv.imshow('img_guassian_blur', img_guassian_blur)
cv.imshow('img_median_blur', img_median_blur)

cv.waitKey(0)

"""
blur(): This function applies a simple averaging filter to the image.
It is effective in reducing high-frequency noise but may not be as effective as Gaussian or median blur in some cases.

GaussianBlur(): This function applies a Gaussian blur to the image.
Gaussian blur is often preferred when the noise in the image is more random and normally distributed.
It tends to preserve edges better than a simple blur.

medianBlur(): This function computes the median of all the pixels under the kernel area and replaces the central pixel with this median value.
Median blur is particularly effective in removing salt-and-pepper noise, which appears as isolated bright and dark pixels in the image.

In summary:
--> If you have Gaussian or normally distributed noise, you might prefer GaussianBlur().
--> If you have salt-and-pepper noise, medianBlur() is often a good choice.
--> If you just want a simple and fast blur without specific noise considerations, blur() could be suitable.
"""