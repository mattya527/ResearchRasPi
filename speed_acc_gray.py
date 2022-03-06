import Adafruit_PCA9685
import RPi.GPIO as GPIO
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from time import sleep,perf_counter

model = load_model('/home/pi/Research/model.h5')

set_freq = 50
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(set_freq)

def convert_deg(deg,freq):
   step = 4096
   max_pulse = 2.4
   min_pulse = 0.5
   center_pulse = (max_pulse - min_pulse) / 2 + min_pulse
   one_pulse = round((max_pulse - min_pulse) /180,2)
   deg_pulse = center_pulse + deg * one_pulse
   deg_num = int(deg_pulse / (1.0 / freq * 1000 / step))
   print('deg:'+str(deg)+'('+str(deg_num)+')')
   return deg_num

def palm():
   
         pwm.set_pwm(0,0,convert_deg(-90,set_freq))
         pwm.set_pwm(3,0,convert_deg(90,set_freq))
         pwm.set_pwm(5,0,convert_deg(90,set_freq))
         pwm.set_pwm(8,0,convert_deg(90,set_freq))
         pwm.set_pwm(12,0,convert_deg(-90,set_freq))
   

def l():
  
         pwm.set_pwm(0,0,convert_deg(-90,set_freq))
         pwm.set_pwm(3,0,convert_deg(90,set_freq))
         pwm.set_pwm(5,0,convert_deg(-90,set_freq))
         pwm.set_pwm(8,0,convert_deg(-90,set_freq))
         pwm.set_pwm(12,0,convert_deg(90,set_freq))
   

def fist():
   
         pwm.set_pwm(0,0,convert_deg(90,set_freq))
         pwm.set_pwm(3,0,convert_deg(-90,set_freq))
         pwm.set_pwm(5,0,convert_deg(-90,set_freq))
         pwm.set_pwm(8,0,convert_deg(-90,set_freq))
         pwm.set_pwm(12,0,convert_deg(90,set_freq))
   

def thumb():
   
         pwm.set_pwm(0,0,convert_deg(-90,set_freq))
         pwm.set_pwm(3,0,convert_deg(-90,set_freq))
         pwm.set_pwm(5,0,convert_deg(-90,set_freq))
         pwm.set_pwm(8,0,convert_deg(-90,set_freq))
         pwm.set_pwm(12,0,convert_deg(90,set_freq))
   

def ok():
   
         pwm.set_pwm(0,0,convert_deg(0,set_freq))
         pwm.set_pwm(3,0,convert_deg(0,set_freq))
         pwm.set_pwm(5,0,convert_deg(90,set_freq))
         pwm.set_pwm(8,0,convert_deg(90,set_freq))
         pwm.set_pwm(12,0,convert_deg(-90,set_freq))
   

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
   return thresh
 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
image_size = (64,64)
temp_ges = None
count = 0
t_count = 0
for i in range(50):
   start_time = perf_counter()
   ret,frame = cap.read()
   if ret == True:
      frame = cv2.resize(frame,(640,480))
      img = divide_frame(frame)
      cv2.imshow("frame",img)
      img = cv2.resize(img,image_size)
      img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      _,img = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
      #img = binarization_image(img)
      #cv2.imshow("HSV",img)
      img = img.reshape(1,64,64,1)
      recog = model.predict(img)
      np.set_printoptions(formatter={'float':'{:.4f}'.format})
      print(recog)
      
      index = np.argmax(recog)
        
      print('Gesture:',index+1)
      if index == 0:
                  palm()
                  print("palm")
      elif index == 1:
                  l()
                  print("l")
                  t_count += 1
      elif index == 2:
                  fist()
                  print("fist")
      elif index == 3:
                  thumb()
                  print("thumb")
      elif index == 4:
                  ok()
                  print("ok")
      else:
                  pass
   
      count += 1    
      print("time:",perf_counter() -start_time)
         

      if cv2.waitKey(1) & 0xFF == ord('q'):
         break
print("{:.4f}".format(t_count / count))
cap.release()
cv2.destroyAllWindows()
