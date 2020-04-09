import cv2
import numpy as np

namefile=input("Inserisci nome file (senza estenzione): ")
cap = cv2.VideoCapture(0)#zero sta per la prima web camere che hai nel coputer e cosi via 1 2 3
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(namefile+".avi", fourcc, 20.0, (640,480))###
while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)###registra quello che vede dalla telecamera in formato datogli sopra
    cv2.imshow('frame',frame)
    cv2.imshow('grigio',gray)

    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
exit()
