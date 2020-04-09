##non capisco cosa devo fare dato che è un ripasso di quello che gia so
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#   = cv2.VideoCapture('people-walking.mp4')##cambia il nome
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
