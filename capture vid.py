# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:32:52 2021

@author: cttc
"""

import cv2
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)

ret,frame = cap.read()

cap.release()
plt.imshow(frame)
plt.show()