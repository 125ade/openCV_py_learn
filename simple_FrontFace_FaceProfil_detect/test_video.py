import numpy as np
import cv2

cap1 = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(1)
cap1.set(3,1280)
cap1.set(4,1024)
while True:
    
    ret1, frame1 = cap1.read()
    #ret2, frame2 = cap2.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)



    #APRE LE FINESTRE
    cv2.imshow('PRIMA TELECAMERA',frame1)
    #cv2.imshow('SECONDA TELECAMERA',frame2)
    cv2.imshow('PRIMA TELECAMERA GRIGIO',gray1)
    #cv2.imshow('SECONDA TELECAMERA GRIGIO',gray2)

    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        # When everything done, release the capture
        cap1.release()
        #cap2.release()
        cv2.destroyAllWindows()
        exit()
        break

