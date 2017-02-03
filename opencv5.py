import cv2
import numpy as np

cap = cv2.VideoCapture(1)

#define codec and create videowriteer object

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/output/output.mp4', fourcc, 30.0, (1280,1024))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame, 0)

        #write out flipped frames
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

