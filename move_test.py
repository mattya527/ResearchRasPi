import RPi.GPIO as GPIO
import Adafruit_PCA9685
from time import sleep

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
   

while True:
   palm()
   sleep(1)
   l()
   sleep(1)
   fist()
   sleep(1)
   thumb()
   sleep(1)
   ok()
   sleep(1)
