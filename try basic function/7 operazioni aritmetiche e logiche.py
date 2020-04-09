import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('logo.png')
##somma immagini
add = img1+img2
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('add 1',add)
##somma pixel a pixel insieme
add = cv2.add(img1,img2)
cv2.imshow('addc',add)
##un immagine sopra l' altra
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted',weighted)

##prende un immagine logo e la sovrappone ad un altra
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img3.shape
roi = img1[0:rows, 0:cols ]
# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('mask',mask)
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img3_fg = cv2.bitwise_and(img3,img3,mask = mask)
dst = cv2.add(img1_bg,img3_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)



cv2.waitKey(0)
cv2.destroyAllWindows()
