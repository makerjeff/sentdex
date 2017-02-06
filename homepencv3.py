# Drawing Shapes and Text

import numpy as np
import cv2

img = cv2.imread('images/cat_02.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0),(150,150), (255,0,0), 5)
cv2.rectangle(img, (15,15), (200,100), (0,255,0), 5)
cv2.circle(img, (50,50), 35, (0,0,255), -1)

# for polygon drawing
pts = np.array([[10,5],[20,30],[200,100],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,150,255), 2)

# for Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV tuts!',(50,300), font, 2, (0,0,0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print 'All windows closed.'