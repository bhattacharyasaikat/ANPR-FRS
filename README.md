#Automatic Number Plate Detection and Face Recognition System

This project is an implementation of an Automatic Number Plate Detection and Face Detection System using Python and OpenCV. The aim of this project is to develop a system that can automatically detect and recognize license plates and human faces in real-time using computer vision techniques, for the purpose of protecting our nation for college project.

##Features

Automatic detection of license plates in images and video streams
Recognition of license plate numbers using Optical Character Recognition (OCR) technology
Detection of human faces in images and video streams
Recognition of faces using deep learning-based face recognition models
Support for multiple languages and character sets

##Requirements

Python 3.x
OpenCV 4.x
Pytesseract
Numpy
imutils
TensorFlow

##Installation

###Clone the repository:
git clone https://github.com/your_username/ANPR-FRS.git

###Install the required packages:
pip install -r requirements.txt

###Download and install the Haar cascades files for license plate and face detection:
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_russian_plate_number.xml
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

###Run the script:
python anpr_frs.py

##Acknowledgments
We would like to acknowledge the following sources that were used in the development of this project:

Haar cascades files for license plate and face detection: https://github.com/opencv/opencv/tree/master/data/haarcascades
TensorFlow FaceNet implementation: https://github.com/davidsandberg/facenet

##License

This project is licensed under the MIT License.
