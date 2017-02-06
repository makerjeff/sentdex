# image and video analysis
import numpy as np
import cv2

img = cv2.imread('images/jffmbl.png', cv2.IMREAD_COLOR)

img[200,250] = (0,255,0)

# roi = img[100:150, 100:150]

# img[100:150, 100:220] = [255,255,255]

#roi = [y1:y2, x1:x2]

# img[220:290, 100:200] = (255,255,255)

plate = img[220:290, 100:200]   #region of license plate

img[0:70, 0:100] = plate

cv2.imshow('image', img)

print 'shape: ' + str(img.shape)
print 'size: ' + str(img.size)  # of pixels
print 'data type: ' + str(img.dtype) #uint8

cv2.waitKey(0)
cv2.destroyAllWindows()