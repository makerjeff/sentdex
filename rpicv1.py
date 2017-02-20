import numpy as np
import cv2

#load images
#image = cv2.imread('images/face.jpg', 1)
image = cv2.imread('_secret_images/family.jpeg')
print 'height: ' + str(np.size(image,0))
print 'width: ' + str(np.size(image,1))


#load cascades
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

#convert images to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w, y+h), (255,0,0), 2)
    roi_gray = gray[y:y+h, x: x+w]
    roi_color = image[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()