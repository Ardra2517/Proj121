import cv2
import time
import numpy as np
#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)
bg = 0

#Capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()
    
#Flipping the background
bg = np.flip(bg, axis=1)
frame=cv2.resize(frame, (640,480))
image=cv2.resize(image, (640,480))

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Flipping the image for consistency
    img = np.flip(img, axis=1)

    #Converting the color from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Generating mask to detect red colour
    #These values can also be changed as per the color
    l_black = np.array([104, 153, 70])
    u_black = np.array([30, 30, 0])
    mask = cv2.inRange(hsv, l_black, u_black)

    #Open and expand the image where there is mask 1 (color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

    #Keeping only the part of the images without the red color 
    #(or any other color you may choose)
    res = cv2.bitwise_and(frame, frame, mask = mask)

f = frame - res
f = np.where(f == 0, image, f)
cap.release()
out.release()
cv2.destroyAllWindows()
