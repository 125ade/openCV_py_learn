import numpy as np
import cv2


img = cv2.imread('x.jpg',cv2.IMREAD_COLOR)
px = img[55,55]#prende il pixel 55 55

print(px) #stampa il colore di px

img[55,55]=[0,0,0]#cambia colore a px

print(px)#stampa px con colore modificato

#specifica una regione del immagine

roi = img [100:150,100:150]
print(roi)#stampa i colori di tutti i pixel della regione presa in considerazione
img [100:150,100:150]=[0,0,0]
print(roi)
#prende una parte del immagine
parte_img=img[37:111,107:194]
img[0:74,0:87]=parte_img

cv2.imshow('immagine',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()
