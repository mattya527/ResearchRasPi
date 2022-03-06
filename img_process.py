import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

pic_path = '/home/pi/Research/test_frame/palm_test.png'
model = load_model('/home/pi/Research/model.h5')
lower = np.array([0,0,210])
upper = np.array([180,255,255])
fig = plt.figure()

def number_of_element(img):
   H = []
   S = []
   V = []
   for i in range(0,32):
      for j in range(0,32):
         H.append(img[i][j][0])
         S.append(img[i][j][1])
         V.append(img[i][j][2])
   return H,S,V

img = cv2.imread(pic_path)

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#img = cv2.bitwise_not(img)
ax3 = fig.add_subplot(2,2,1)
plt.imshow(img)
img = cv2.resize(img,(32,32))
H,S,V = number_of_element(img)
new_h = sorted(H)

ax1 = fig.add_subplot(2,2,2)
ax1.set_title("Hue")
plt.hist(new_h,bins=180)
skinRegionHSV = cv2.inRange(img,lower,upper)
img = cv2.blur(skinRegionHSV,(2,2))
_,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)

for i in range(30,32):
    for j in range(img.shape[1]):
       img[i][j] = 0

ax2 = fig.add_subplot(2,2,3)
plt.imshow(img) 
plt.show()
img = img.reshape(1,32,32,1)
recog = model.predict(img)
np.set_printoptions(formatter={'float':'{:.4f}'.format})
print(recog)

