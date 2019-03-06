# face-recognition-based-attendance
This is python based project using opencv and pandas to create an attendance system based on face recognition, where the attendance is continuously stored in an excel sheet

This project was accomplished from the face recognition tutorial project mentioned below

https://github.com/informramiz/opencv-face-recognition-python


A ton thanks to its creators.

Requirements:
The project was succesfully tested on the following environement

1. Python 3.6.7
2. Numpy 1.14.2
3. Opencv 3.4.2
4. pandas 0.23.4
5. python-dateutil 2.7.5


Steps to run the project:

1. Go to the folder training- data and run the python script capture.py
        The camera interface will open. If not try changing the parameter of Vidoecapture() method from 0 to 1 or viceversa. 
        The person should face the camera and continuosly press space bar. A folder named 'test-data' will be created and photos will be stored inside it. Rename the folder to s1. 


Now again run the script with second person and change the folder to s2. 
        Conitnue this as many times to include that much people for face recognition as s3, s4, s5 etc. 
        

Enter the names of the persons in the same order in the attendance_registed.xlxs file. Also add these names in the same order replacing 'name1', 'name2' etc. in the subjects list in the file attendance.py
     

           
 2. Now the data is prepared in required order. Run the training.py script and let the training be complete. Now you will see a model.xml file generated in the main folder. This is the face data of the trained faces.
 
 3. Now sort the names in the attendance_register.xlxs file alphabetically (DO NOT do this in subjects list in attendance.py)
 
 
 4. Now its time for attendance marking. Go to main folder and run capture.py script. Click one picture each of the persons who are present (only those persons whose faces were already trained). These pictures will be stored in test-data folder
 
 5. Now run the attendance.py script. After prediction you will see the names of the persons who are present, displayed in the screen. Also a new coloumn will be added in attendance_register.xlxs file with todays date marking either 'p' or 'a'.
 
 _________________________________________________________________________________________________________________________________
 _________________________________________________________________________________________________________________________________

