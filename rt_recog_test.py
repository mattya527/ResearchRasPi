
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from time import sleep,perf_counter

model = load_model('/home/pi/Research/model.h5')


def divide_frame(frame):
   height,width,channels = frame.shape
   upper_right = frame[0:height//2,0:width//2]
   return upper_right
   
def binarization_image(img):
   lower = np.array([0,0,210],dtype='uint8')
   upper = np.array([180,255,255],dtype='uint8')
   skinRegionHSV = cv2.inRange(img,lower,upper)
   img_bin = cv2.blur(skinRegionHSV,(2,2))
   _,thresh = cv2.threshold(img_bin,0,255,cv2.THRESH_BINARY)
   #for i in range(27,32):
    #  for j in range(img.shape[1]):
      #   img[i][j] = 0
   return thresh
 
cap = cv2.VideoCapture(0)
image_size = (32,32)
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('demo.mov',fourcc,5.0,(32,32),False)
while True:
   start_time = perf_counter()
   ret,frame = cap.read()
   if ret == True:
      frame = cv2.resize(frame,(640,480))
      img = divide_frame(frame)
      
      img = cv2.resize(img,image_size)
      
      img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
      img = binarization_image(img)
      
      
      img2 = img.reshape(1,32,32,1)
      recog = model.predict(img2)
      np.set_printoptions(formatter={'float':'{:.4f}'.format})
      print(recog)
      index = np.argmax(recog)
      print('Gesture:',index+1)
      print('time:',perf_counter() - start_time)
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(img,'aaa',(0,0),font,4,(0,255,255),2,cv2.LINE_AA)
      cv2.imshow("bin",img)
      out.write(img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
out.release()
cv2.destroyAllWindows()
