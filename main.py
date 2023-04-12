import cv2
import numpy as np
import os
from pytesseract import pytesseract
import requests
import pandas as pd

frameWidth = 640    
franeHeight = 480   

plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

minArea = 500

cap =cv2.VideoCapture("Testing Footage.mp4")


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

# -----------OCR-----------------


class OCR:
    def __init__(self):
       self.path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

    def extract(self,filename):
        try:
            pytesseract.tesseract_cmd=self.path
            text = pytesseract.image_to_string(filename)
            return text
        except Exception as e:
            print(e)
            return "Error"
        

ocr = OCR()

# ---------OCR-------------
pic = cv2.imread("photos0.jpg")

kernel = np.ones((1,1),np.uint8)
pic= cv2.dilate(pic, kernel, iterations=1)
pic = cv2.erode(pic, kernel, iterations=1)
plate_gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
(thresh,imgRoi) = cv2.threshold(plate_gray,127,255,cv2.THRESH_BINARY)
text = ocr.extract(pic)
num = []
j = 0

for i in text:
    if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        num.append(i)
        j += 1

NumberPlate = ''.join(num)
print(NumberPlate)

#---------------------RC VALIDATION -------------------#

import requests
import datetime

url = "https://vehicle-rc-information.p.rapidapi.com/"

payload = {"VehicleNumber": "WB20AX4245"}
headers = {
"content-type": "application/json",
	"X-RapidAPI-Key": "5f6cc5ecf9mshf3a63ebe7e35fe8p10f498jsnb1fd2bf679e5",
	"X-RapidAPI-Host": "vehicle-rc-information.p.rapidapi.com"
}

def check_validity(response, field): # define a function that takes a response object and a field name as arguments
  response_dict = response.json() # convert response text to dictionary
  valid_upto = response_dict["result"][field] # get valid_upto value for the given field
  valid_date = datetime.datetime.strptime(valid_upto, "%Y-%m-%d") # convert valid_upto string to datetime object
  today = datetime.datetime.now() # get current date and time
  if valid_date > today: # compare valid_date with today
    return True # return True if valid_date is later than today
  else:
    return False # return False if valid_date is earlier than or equal to today

response = requests.request("POST", url, json=payload, headers=headers)

#print(response.text)
response_dict = response.json() # convert response text to dictionary
owner_name = response_dict["result"]["owner_name"] # get owner name
fuel_type = response_dict["result"]["fuel_type"] # get fuel type
seat = response_dict["result"]["seating_capacity"]
registration =  response_dict["result"]["fitness_upto"]
insurance = response_dict["result"]["insurance_validity"]
pollution =  response_dict["result"]["puc_valid_upto"]
#request
fitness_validity = check_validity(response, "fitness_upto") # fitness_upto field and assign the result to a variable
insurance_validity = check_validity(response, "insurance_validity") # insurance_validity field and assign the result to a variable
puc_validity = check_validity(response, "puc_valid_upto") #  puc_valid_upto field and assign the result to a variable
print("Car Validation: ",fitness_validity) 
print("Insurance Validation: ",insurance_validity) 
print("pollution status:",puc_validity) 


print("Car Owner Name: ",owner_name) 
print("Fuel type: ",fuel_type) 
print("Seat capacity: ",seat)



#----------------SMS alert-------------------#


# sms for Insurance validation

if insurance_validity is False:
   
    url = "https://sms77io.p.rapidapi.com/sms"
    payload = "to=%2B491771783130&p=%3CREQUIRED%3E&text=e-challan%20for%20Insurance%20failure"
    headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "5f6cc5ecf9mshf3a63ebe7e35fe8p10f498jsnb1fd2bf679e5",
    "X-RapidAPI-Host": "sms77io.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)

# sms for registration validation
if fitness_validity is False:
   
    url = "https://sms77io.p.rapidapi.com/sms"
    payload = "to=%2B491771783130&p=%3CREQUIRED%3E&text=e-challan%20for%20invalid%20registration"
    headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "5f6cc5ecf9mshf3a63ebe7e35fe8p10f498jsnb1fd2bf679e5",
    "X-RapidAPI-Host": "sms77io.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)

# sms for pollution validation
if puc_validity is False:
   
    url = "https://sms77io.p.rapidapi.com/sms"
    payload = "to=%2B491771783130&p=%3CREQUIRED%3E&text=e-challan%20for%20pollution"
    headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "5f6cc5ecf9mshf3a63ebe7e35fe8p10f498jsnb1fd2bf679e5",
    "X-RapidAPI-Host": "sms77io.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
# --------Saving the data-----------

data ={'Owner Name' :[owner_name],
      'Model Number':[],
      'Registration Validity':[registration],
      'PUC':[pollution],
      'Insurance':[insurance]
      }

df = pd.DataFrame(data,columns=['Owner Name','Model Number','Registration Validity','PUC','Insurance'])


print("the df is",df)
df.to_csv("test.csv")
xt6
