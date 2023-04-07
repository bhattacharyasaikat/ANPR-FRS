import cv2
import numpy as np
import os
from pytesseract import pytesseract


frameWidth = 640    
franeHeight = 480   

plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

minArea = 500

cap =cv2.VideoCapture("both.mp4")

cap.set(4,franeHeight)
cap.set(10,150)

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
            #cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('Frame',img)

    if cv2.waitKey(30) & 0xFF==ord('q'):
       # cv2.imwrite("C:\\Users\\HP\Desktop\\Python\\Number_Plate_Detection\\photos"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.waitKey(200)
        break
cap.release()
cv2.destroyAllWindows()

   