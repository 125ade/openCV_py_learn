import numpy as np
import cv2
face_frontal = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_profile = cv2.CascadeClassifier('haarcascade_profileface.xml')
eye_sx = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml') #non distingue quale occhio
eye_dx = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')#a volte però si distingue
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

vers_cv = "  OpenCV " + cv2.__version__

while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print("img__________________________________________________________")
    #print(img)
    #print("gray_________________________________________________________")
    #print(gray)
    cv2.putText(img,vers_cv,(5,15), font, 0.5, (0,0,0),1,cv2.LINE_AA)
    
    #trova il volto frontale    
    faces_f = face_frontal.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces_f:
        #print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,'FRONTE',(x+5,y+15), font, 0.5, (255,0,0),1,cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]        
        
        #trova l' occhio sinistro
        eyes_s = eye_sx.detectMultiScale(roi_gray,1.1,5)
        for (ex,ey,ew,eh) in eyes_s:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            cv2.putText(roi_color,'sx',(ex+5,ey+15), font, 0.5, (0,0,255),1,cv2.LINE_AA)

        #trova l' occhio destro   
        eyes_d = eye_dx.detectMultiScale(roi_gray,1.1,5)
        for (ex,ey,ew,eh) in eyes_d:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            cv2.putText(roi_color,'dx',(ex+5,ey+15), font, 0.5, (0,0,255),1,cv2.LINE_AA)

        #trova il sorriso
        smile = smile_cascade.detectMultiScale(roi_gray,1.1,5)
        for (ex,ey,ew,eh) in smile:
            cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(255,255,255),2)
            cv2.putText(roi_color,'BOCCA',(ex+5,ey+15), font, 0.5, (255,255,255),1,cv2.LINE_AA)

    #trova il volto di profilo
    faces_p = face_profile.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces_p:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,'PROFILO',(x+5,y+15), font, 0.5, (0,255,0),1,cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        #trova l' occhio sinistro
        eyes_s = eye_sx.detectMultiScale(roi_gray,1.1,5)
        for (ex,ey,ew,eh) in eyes_s:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            cv2.putText(roi_color,'sx',(ex+5,ey+15), font, 0.5, (0,0,255),1,cv2.LINE_AA)

        #trova l' occhio destro   
        eyes_d = eye_dx.detectMultiScale(roi_gray,1.1,5)
        for (ex,ey,ew,eh) in eyes_d:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            cv2.putText(roi_color,'dx',(ex+5,ey+15), font, 0.5, (0,0,255),1,cv2.LINE_AA)
            
    
    cv2.imshow('img',img)
    #come scrivere
    
    k = cv2.waitKey(20) & 0xFF
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        exit()
        break


