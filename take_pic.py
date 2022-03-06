import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)
image_size = (32,32)

def divide_frame(frame):
   height,width,channels = frame.shape
   upper_right = frame[0:height//2,0:width//2]
   return upper_right

while True:
   ret,frame = cap.read()
   if ret == True:
      frame = cv2.resize(frame,(640,480))
      img = divide_frame(frame)
      cv2.imshow('frame',img)
      img = cv2.resize(img,image_size)
     
      if cv2.waitKey(1) & 0xFF == ord('s'):
         cv2.imwrite('/home/pi/Research/test_frame/palm_test.png',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()
