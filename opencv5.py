import argparse
import cv2
import numpy as np

#init argparse
ap = argparse.ArgumentParser()
ap.add_argument("-O", "--output", required=True,
                help="path to output video. must be unique")
args = vars(ap.parse_args())


#create video capture
cap = cv2.VideoCapture(1)



#define codec and create videoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output/' + args["output"], fourcc, 10.0, (1280,1024))

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret==True:
        # frame = cv2.flip(frame, 1)

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

