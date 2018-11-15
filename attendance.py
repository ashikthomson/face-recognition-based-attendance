import cv2
import os
import numpy as np
import pandas as pd
import time


subjects = ['','Name 1','Name 2','Name 3']

face_recognizer_1 = cv2.face.LBPHFaceRecognizer_create()
face_recognizer_1.read("model.xml")


# In[8]:

#function to draw rectangle on image 
#according to given (x, y) coordinates and 
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#function to draw text on give image starting from
#passed (x, y) coordinates. 
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


# First function `draw_rectangle` draws a rectangle on image based on passed rectangle coordinates. It uses OpenCV's built in function `cv2.rectangle(img, topLeftPoint, bottomRightPoint, rgbColor, lineWidth)` to draw rectangle. We will use it to draw a rectangle around the face detected in test image.
# 
# Second function `draw_text` uses OpenCV's built in function `cv2.putText(img, text, startPoint, font, fontSize, rgbColor, lineWidth)` to draw text on image. 
# 
# Now that we have the drawing functions, we just need to call the face recognizer's `predict(face)` method to test our face recognizer on test images. Following function does the prediction for us.

# In[9]:

#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject


def detect_face(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]







def predict(test_img):
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    face, rect = detect_face(img)

    #predict the image using our face recognizer 
    label, confidence = face_recognizer_1.predict(face)
    #get name of respective label returned by face recognizer
    label_text = subjects[label]
    
    #draw a rectangle around face detected
    draw_rectangle(img, rect)
    #draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1]-5)
    
    return img,label_text

# Now that we have the prediction function well defined, next step is to actually call this function on our test images and display those test images to see if our face recognizer correctly recognized them. So let's do it. This is what we have been waiting for. 

# In[10]:

students = os.listdir("test-data") 
student_count = len(students)    #Count the number of files in test folder to find the total number of students
print (student_count)

print("Predicting images...")
names=[]

for i in range(1,student_count+1):
	test_img1=cv2.imread("test-data/test"+str(i)+".jpg")
	predicted_img1,name = predict(test_img1)
	names.append(name)
	cv2.imshow(name, cv2.resize(predicted_img1, (400, 500)))
	print (i)
	


print("Prediction complete and the students present are \n")
names=sorted(names, key=str.lower)
print(names)



attendance=[]
df = pd.read_excel('attendance_register.xlsx',sheet_name='sheet1') # can also index sheet by name or fetch all sheets
classlist = df['Names'].tolist()

print("total students of the class are \n")
print (classlist)
j=0
for i in classlist:
	

	if names[j] != i:
		attendance.append('a')
		
	else:
		attendance.append('p')
		if j < (len(names)-1):
			j=j+1
	
today_date =time.strftime("%m/%d/%Y")	
	
	
	

df [today_date] = attendance


df.to_excel("attendance_register.xlsx",sheet_name='sheet1',index=False);	

	
			
print (attendance)	


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()