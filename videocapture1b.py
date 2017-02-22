import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('videos/vidcap1b_8_15fps.mp4', fourcc, 15.0, (640,480))

#while(True) = python3 syntax
while True:
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print 'Capture closed.'