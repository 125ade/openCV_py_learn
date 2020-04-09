import numpy as np
import cv2 as cv
#input nome file
nome = input('nome dell immagine da visualizzare in scala di grigio: ')
#load an color image in grayscale
img = cv.imread(nome,0) #prende l' immagine messi5.jpg
cv.imshow(nome,img)#fa vedere l' immagine
k = cv.waitKey(0)#aspetta la chiave di uscita
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('grigio '+nome,img)
    cv.destroyAllWindows()
exit()
