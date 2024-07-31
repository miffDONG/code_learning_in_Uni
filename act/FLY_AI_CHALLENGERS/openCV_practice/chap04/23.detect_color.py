import numpy as np
import cv2
from cv2 import SimpleBlobDetector
blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)    	# 색
image = np.zeros((480, 640, 3), np.uint8)    					# 
image[:] = (255, 255, 255)

pt1, pt2 = (150, 135), (400, 150)                   		        # 
pt3, pt4 = (400, 300), (300, 250)
roi = (50, 200, 200, 100)

cv2.circle(image,pt1,100,blue,-1)                         #  
cv2.circle(image,pt2,50,green,-1)
cv2.circle(image,pt3,70,red,-1)
cv2.circle(image,pt4,30,green,-1)                   #  

cv2.imshow('circle & Rectangle', image)							# 
cv2.waitKey(0)
cv2.destroyAllWindows()											# 

cv2.imwrite("images/color_detect.jpg", image)

Detector = SimpleBlobDetector()