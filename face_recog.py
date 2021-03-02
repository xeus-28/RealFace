# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:06:28 2021

@author: cttc
"""
import  cv2
import numpy as np
import urllib

import matplotlib.pyplot as plt

URL = "http://192.168.43.1:8080/shot.jpg" #this is used by useing mobile phone
'''vid = cv2.VideoCapture(0) # useing camera 
ret,frame = vid.read()'''    #
face_data = "haarcascade_frontalface_default.xml"
classifier = cv2.CascadeClassifier(face_data)  #used to find the cordinate point of the face
data = []

while True:             #we need a true condition 

    img_url = urllib.request.urlopen(URL)
    image = np.array(bytearray(img_url.read()),np.uint8)
    frame = cv2.imdecode(image,-1)
    
    face = classifier.detectMultiScale(frame,1.5,5) # scale factor and minimum neighour
    
    if face is not None :
        for x,y,w,h in face:
            face_img = frame[y:y+h,x:x+w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
            
            if len(data) <=100:
            
                data.append(face_img)
            else:
                cv2.putText(frame,'complete',(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
                
    cv2.imshow('capture',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()


name = input("enter your name : ")
c = 0

for i in data:
    cv2.imwrite("images/" +name+'_'+str(c)+'.jpg',i)
    c = c+1
    
for i in range(3,10):
    plt.imshow(data[i])
    plt.show()
    