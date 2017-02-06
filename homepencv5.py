import numpy as np
import cv2

img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainsvmimage.png')

# add = img1 + img2 # not ideal
# add = cv2.add(img1, img2) #comes out the way it's meant to.
# weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# cv2.imshow('add', weighted)



cv2.waitKey(0)
cv2.destroyAllWindows()