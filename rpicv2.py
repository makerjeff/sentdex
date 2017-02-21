#SCAN MANY FACES and write back out

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

img = cv2.imread('images/manyfaces.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    #TODO: figure out why this is necessary
    roi_gray = gray_img[y:y+h, x:x+w]   #(?) creates a ROI range
    roi_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)   # uses ROI of face to detect eyes (efficiency?)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
#cv2.imwrite('images/manyfaces_result.jpg', img)
cv2.destroyAllWindows()
