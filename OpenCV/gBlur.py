import cv2
#from matplotlib import pyplot as plt
cap=cv2.VideoCapture(-1)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
th=127
max_val=255

while True:
    ret, Fr= cap.read()
    frame = cv2.resize(Fr, (400, 300))
    img=frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,o1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #RGBA=cv2.cvtColor(frame,cv2.COLOR_Luv2RGB)
    #ret,trunc = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    img2gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #ret , mask = cv2.threshold(img2gray, 235, 255,cv2.THRESH_BINARY_INV)
    #img_fg= cv2.bitwise_and(img, img, mask=mask)
    imgt = cv2.adaptiveThreshold(img2gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    gauImgM= cv2.adaptiveThreshold(img2gray , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 2)
    #plt.hist(img.ravel(),256,[0,256]); plt.show()
    gBlur= cv2.GaussianBlur(gauImgM,(15,15),0)
    median= cv2.medianBlur(gauImgM,15)
    
    nRes= cv2.add(gBlur,gauImgM)
    cv2.imshow('original',img)
    cv2.imshow('nRes' ,nRes)
    #cv2.imshow('fg' , img_fg)
    cv2.imshow('GAUSSIAN' , imgt)
    cv2.imshow('GAUSSIAN mean' , gauImgM)
    #out.write(Fr)
    cv2.imshow('OTSU',o1)
    cv2.imshow('median',median)
    #cv2.imshow('RGBA',RGBA)
    cv2.imshow('gBlur',gBlur)
    #cv2.imshow('trunc',trunc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
#out.release()
cv2.destroyAllWindows()


