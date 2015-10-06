import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)
i = 0
cap.set(3, 352)
cap.set(4, 288)
t_init = datetime.datetime.now()
while(i < 10):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    i += 1

t_final = datetime.datetime.now()

print(t_final - t_init)
