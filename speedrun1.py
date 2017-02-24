# http://rpihome.blogspot.com/2015/03/face-detection-with-raspberry-pi.html

import cv2
import time     #use time.clock() for benchmarking precision.



# load an image
image = cv2.imread('_secret_images/family.jpg')

# load cascades
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# convert to grayscale for computation
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


start_time = time.clock()   #log time before computation
# look for faces (image, scaleFactor, minNeighbors)
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
end_time = time.clock()     #log time after computation

print 'Found ' + str(len(faces)) + ' face(s) in ' + str(end_time - start_time)

# for each 4-tuple in 'faces' array
for (x,y,w,h) in faces:
    # draw a rectangle (starting point), (ending point), color, line width
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)

    #TODO: setup ROI for sub regions to scan for other features recursively, like eyes.



#draw image or write to file.
cv2.imshow('"iamge"', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
