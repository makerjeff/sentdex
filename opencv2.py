import cv2
import numpy as np

screen_0_cap = cv2.VideoCapture(0)
screen_1_cap = cv2.VideoCapture(1)

# while True:
while (screen_0_cap.isOpened()):
    ret, frame = screen_1_cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

screen_0_cap.release()
cv2.destroyAllWindows()