#!/usr/bin/env python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/cat_01.jpg', cv2.IMREAD_GRAYSCALE)

# CV2 method ================
cv2.imshow('a window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # MATPLOTLIB method =========
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100],[80, 100], 'red', linewidth=2)
# plt.show()

cv2.imwrite('images/conv_cat_01.jpg', img)
