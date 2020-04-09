import numpy as np
import cv2 as cv
nome = input('nome del file: ')
cap = cv.VideoCapture(nome)
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        exit()
        break

