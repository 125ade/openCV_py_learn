import cv2
import matplotlib
import numpy as np

img = cv2.imread('b.jpg', cv2.IMREAD_COLOR)

#linea
cv2.line(img,(0,0),(150,150),(255,0,0),5)##immagine/video dove scrivere , () dove inizia, () dove finisce la riga, () colore in bgr, spessore in px

#rettangolo
cv2.rectangle(img, (150,150) , (200,200) , (0,255,0) , 5)

#cerchio
cv2.circle(img, (100,63) , 55, (0,0,255), -1) #numeri negativi vuol dire che sono colorati al interno

#poligono
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

#come scrivere
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv tutorial!',(0,130), font, 1, (200,255,255),2,cv2.LINE_AA)

#fa vedere l' immagine
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
