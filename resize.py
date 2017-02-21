import numpy as np
import cv2

image = cv2.imread('images/jurassic-park-tour-jeep.jpg')

#rows, columns, channels (instead of width, height)
# print image.shape[0]
# print image.shape[1]
# print image.shape[2]
print image.shape

#ratio and dimensions
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))

#resized
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('resized', resized)
# cv2.imshow('original', image)
cv2.waitKey(0)