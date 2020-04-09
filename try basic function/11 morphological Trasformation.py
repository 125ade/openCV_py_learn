import numpy as np
import cv2
##
### cerchiamo di eliminare le interferenze che i filtri creano###
##
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue setta il valore ###prende solo i colore rosso il resto lo butta###
    lower_red = np.array([150,150,0])
    upper_red = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res= cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilatation = cv2.dilate(mask, kernel, iterations = 1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

############################ DA IMPLEMENTARE ##############################################
    # It is the difference between input and Opening of the image
    #cv2.imshow('Tophat', tophat)
    # It is the difference between the closing of the input immage and input image
    #cv2.imshow('Blackhat',blackhat)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilatation',dilatation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    
    k = cv2.waitKey(20) & 0xFF
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        exit()
        break
