# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:11:49 2025

@author: Mike
"""

#Order of changing capturing parameters should be:

#width
#height
#fps
#[optional] native backend modes / formats.
#You have missed fps.
#For MSMF mode responds for H/W acceleration.
import keyboard
import numpy as np
import cv2#https://github.com/opencv/opencv/issues/12822
import calendar
import datetime
from datetime import datetime
import os
import time

def save_image(img):
    HOMEDIR = os.environ['HOMEPATH']
    print ("HOMEDIR ",HOMEDIR)
    pth='C:\\temp\\camera\\'
    now = datetime.now()
    if len(str(now.month))==1:
        month = "0"+str(now.month)
    else:
        month=str(now.month)
    if len(str(now.day))==1:
        day = "0"+str(now.day)
    else:
        day=str(now.day) 
    whatever  = (pth + (str(now.year)[2:4] + month + day + "\\"))
    f = " " 
    now = datetime.now()
    if len(str(now.hour))==1:
        hournow = "0"+str(now.hour)
    else:
         hournow = str(now.hour)
    if len(str(now.minute))==1:
        minnow = "0"+str(now.minute)
    else:
        minnow = str(now.minute)
    if len(str(now.second))==1:
        secondnow = "0"+str(now.second)
    else:
        secondnow = str(now.second)
    
    #cv2.imshow("img saved",img)
    f = whatever + hournow + minnow + secondnow + ".png"  
    print ("file saved to ",f)
    cv2.imwrite(f,img)
     
    return f

from cv2_enumerate_cameras import enumerate_cameras#https://pypi.org/project/cv2-enumerate-cameras/

for camera_info in enumerate_cameras(cv2.CAP_MSMF):
    print(f'{camera_info.index}: {camera_info.name}')
    
cam = cv2.VideoCapture(0)# cv2.CAP_DSHOW)
print("cam.getBackendName() ",cam.getBackendName())
size=(int(1920/8), int(1080/8))
print("cam.set(cv2.CAP_PROP_FRAME_WIDTH, size[0] )",cam.set(cv2.CAP_PROP_FRAME_WIDTH, size[0]))
print("cam.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1]) ",cam.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1]))
_ret, img = cam.read()
#_ret = True
#cv2.namedWindow("img")
#cv2.resizeWindow('img', size[0],size[1])
#cv2.imshow("img <q> quit ", img)
while _ret:
    ret, img = cam.read()
    cv2.imshow("img <q> quit <s> save img ", img)
    if not ret:
        print("failed to grab img")
        break
    k = cv2.waitKey(1000)
    if keyboard.is_pressed('q'):
        # q pressed
        print("q key, closing...")
        break
    if keyboard.is_pressed('s'):
        # s pressed
        save_image(img)

cam.release()
cv2.destroyAllWindows()