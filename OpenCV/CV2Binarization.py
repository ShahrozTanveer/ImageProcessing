#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:08:57 2019

@author: pysharoz
"""

import cv2 as cv
cap=cv.VideoCapture(0)
while True:
    ret, frame= cap.read()
    Fr = cv.resize(frame, (400, 300))
    laplacian= cv.Laplacian(Fr,cv.CV_64F) # reSize
    sobelx= cv.Sobel(Fr,cv.CV_64F,1,0,ksize=5)
    #sobely= cv.Sobel(Fr,cv.CV_64F,0,1,ksize=5)
    edges= cv.Canny(Fr,100,200)
    gray=cv.cvtColor(Fr,cv.COLOR_BGR2GRAY)
    gauImgM= cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 2)
    cv.imshow('original',Fr)
    cv.imshow('gauImgM',gauImgM)
    #cv.imshow('sobelx',sobelx)
    #cv.imshow('sobely',sobely)
    cv.imshow('edges',edges)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#out.release()
cv.destroyAllWindows()
cv.destroyAllWindows()

