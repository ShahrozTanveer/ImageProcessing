'''import cv2
img= cv2.imread('lena_color_512.tif',0)
cv2.imwrite('lena_grey.jpg',img)
cv2.imshow('Output Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
'''import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena_color_512.tif',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([100,200],[200,100],'c',linewidth=5)
plt.plot([100,200],[200,100],'ro',linewidth=5)
plt.show()'''

import cv2
cap=cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
th=127
max_val=255

while True:
    ret, Fr= cap.read()
    frame = cv2.resize(Fr, (500, 400))
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,o1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    RGBA=cv2.cvtColor(frame,cv2.COLOR_Luv2RGB)
    ret,trunc = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    
    #out.write(Fr)
    cv2.imshow('OTSU',o1)
    cv2.imshow('frame',frame)
    cv2.imshow('RGBA',RGBA)
    cv2.imshow('gray',gray)
    cv2.imshow('trunc',trunc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#out.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()

