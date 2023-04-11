import cv2
import numpy as np
import os
from pytesseract import pytesseract


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
print(text)
num = []
j = 0

for i in text:
    if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        num.append(i)
        j += 1

NumberPlate = ''.join(num)
print(NumberPlate)




#---------
