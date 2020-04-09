import numpy as np
import cv2

img  = cv2.imread('bookpage.jpg')

retval,threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)#img immagine da prendere 12 numero di spartizione del colore 255 massimo colore 

grayscales = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayscales, 12, 255, cv2.THRESH_BINARY)

gaus= cv2.adaptiveThreshold(grayscales, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, otsu = cv2.threshold(grayscales,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('immagine di partenza', img)
cv2.imshow('immagine modificata con aumento di luce',threshold)
cv2.imshow('immagine modificata con aumento di luce IN SCALA DI GRIGIO',threshold2)
cv2.imshow('gaus',gaus)##alcune volte funziona meglio gaus altre otsu
cv2.imshow('otsu',otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
exit()
