import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
    edges = cv2.Canny(frame, 100, 150)##per aggiustare il minimo è 100 e il massimo è 150

    
    cv2.imshow('originale_frame',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)

    
    k = cv2.waitKey(20) & 0xFF
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        exit()
        break
