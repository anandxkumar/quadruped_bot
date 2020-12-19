# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:00:56 2020

@author: anand
"""

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

print(cap.isOpened())
k=cv2.CAP_PROP_FRAME_WIDTH
y=cv2.CAP_PROP_FRAME_HEIGHT
while True :
    
    ret, frame= cap.read()
    if ret==True :
        print(cap.get(k))
        print(cap.get(y))
        out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',gray )
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()