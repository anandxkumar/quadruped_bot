# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:39:03 2020

@author: anand
"""

import cv2

img = cv2.imread('lema.JPEG',0)

print(img)

cv2.imshow('image',img)
k=cv2.waitKey(0)

if k==27 :    
    cv2.destroyAllWindows()

cv2.imwrite('Anand.png',img)