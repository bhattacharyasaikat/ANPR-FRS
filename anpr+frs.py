import cv2
import numpy as np
import os
from pytesseract import pytesseract
import pandas as pd

frameWidth = 640    
franeHeight = 480   

plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

minArea = 500

cap =cv2.VideoCapture("footage.mp4")


# cap.set(4,franeHeight)
# cap.set(10,150)

while True:
    success , img  = cap.read() #plate
    
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #plate

    #img = cv2.imread()
    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)
    faces = face_cascade.detectMultiScale(imgGray,1.3, 5)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            imgRoi = img[y:y+h,x:x+w]
            

    for (x,y,w,h) in faces:
        area1 = w * h
        if area1 > minArea:
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
            imgFace = img[y:y+h,x:x+w]


    cv2.imshow('Frame',img)
    count=0
    if cv2.waitKey(10) & 0xFF==ord('q'):
       cv2.imwrite("C:\\Users\\HP\\Desktop\\abc\\faces"+str(count)+".jpg",imgFace)
       cv2.imwrite("C:\\Users\\HP\\Desktop\\abc\\photos"+str(count)+".jpg",imgRoi)
       count = count + 1
       cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
       cv2.waitKey(200)
       break
cap.release()
cv2.destroyAllWindows()


   
