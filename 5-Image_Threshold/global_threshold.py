import cv2 as cv

img = cv.imread('bear.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# global threshold
ret, thresh = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY)

"""
retval, threshold_output = cv2.threshold(src, thresh, maxval, type[, dst])

'src':
This is the source (input) image, which should be a single-channel (grayscale) image.

'thresh':
This is the threshold value.
Pixels with intensity values greater than this threshold will be set to a certain value (specified by maxval),
and those below the threshold will be set to another value (usually 0).

maxval:
This is the maximum value to be used with the binary and binary inverted thresholding types.
It is the value assigned to pixels that are greater than the threshold.

type:
This parameter specifies the type of thresholding to be applied.
It can take one of the following values:

cv2.THRESH_BINARY: Binary thresholding (pixel values below the threshold are set to 0, and values above are set to maxval).
cv2.THRESH_BINARY_INV: Inverted binary thresholding (opposite of cv2.THRESH_BINARY).
cv2.THRESH_TRUNC: Threshold truncated (values above the threshold are set to the threshold, and values below remain unchanged).
cv2.THRESH_TOZERO: Set to zero (values below the threshold are set to 0, and values above remain unchanged).
cv2.THRESH_TOZERO_INV: Inverted set to zero (values below the threshold remain unchanged, and values above are set to 0).
dst (optional): This is the output image of the same size and type as src. It is not necessary to pass this parameter; if not provided, the function will modify the input image in place.

The function returns two values:
retval: The threshold value that was used (useful in adaptive thresholding).
threshold_output: The thresholded image.

"""

cv.imshow('img', img)
cv.imshow('img_gray', img_gray)
cv.imshow('thresh', thresh)
cv.waitKey(0)