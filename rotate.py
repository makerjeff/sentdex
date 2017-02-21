import numpy as np
import cv2

image = cv2.imread('images/jurassic-park-tour-jeep.jpg')

#rows, columns, channels (instead of width, height)
print image.shape

#slice out a tuple of 'rows' and 'columns'
(h,w) = image.shape[:2]
center = (w/2, h/2)

# rotate image
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('rotated', rotated)
cv2.waitKey(0)