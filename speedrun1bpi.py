# http://rpihome.blogspot.com/2015/03/face-detection-with-raspberry-pi.html
# NOTE: this will only run on a raspberry pi with a picamera attached.

import io
import picamera
import cv2
import numpy as np
import time

# create a stream for the photo
stream = io.BytesIO()

# grab the picture at 320x240
with picamera.PiCamera() as camera:
    camera.resolution = (320,240)
    camera.capture(stream, format='jpeg')

# convert pic to numpy array
buf = np.fromstring(stream.getvalue(), dtype=np.uint8)

# create opencv image (same as imread arguments (file or buffer, 1 (color) or 0 (gray) or -1 unchanged)
image = cv2.imdecode(buf, 1)

# load cascade
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# face detection with clocked response times
start_time = time.clock()
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
end_time = time.clock()

# CLI FEEDBACK
print 'Found ' + str(len(faces)) + ' face(s) in ' + str(end_time - start_time) + ' seconds. '

# draw rectangle around every face found
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w, y+h), (255,0,0), 2)

cv2.imwrite('result1.jpg', image)
