import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue setta il valore ###prende solo i colore rosso il resto lo butta###
    lower_red = np.array([150,150,0])
    upper_red = np.array([180,255,255])

    #dark_red = np.uint8([[[12,22,121]]])
    #dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res= cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)    
    k = cv2.waitKey(20) & 0xFF
    if k == ord('q'):
        ap.release()
        cv2.destroyAllWindows()
        exit()
        break

