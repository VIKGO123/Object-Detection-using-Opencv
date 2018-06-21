import cv2
import numpy as np

img=cv2.imread("C:/Users/hp/Desktop/paint7.jpg")
cv2.imshow("original",img)
cv2.waitKey(0)

gray=cv2.imread("C:/Users/hp/Desktop/paint7.jpg",0)
cv2.waitKey(0)

#find canny edge
edged=cv2.Canny(gray,30,200)
cv2.imshow("canny edged",edged)
cv2.waitKey(0)
#Finding contour
_,contours,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#"""WE CAN USE INPLACE OF EXTERNAL LIST OR TREE """

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print (len(approx))
    if len(approx)==5:
        print ("pentagon")
        cv2.drawContours(img,[cnt],0,(255,0,0),-1)
        cv2.putText(img,'pentagon',(cnt[0][0][0],cnt[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,1,(100,170,0),1)
    elif len(approx)==3:
        print ("triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
        cv2.putText(img,'triangle',(cnt[0][0][0],cnt[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,1,(100,170,0),1)
    elif len(approx)==4:
        print ("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
        cv2.putText(img,'square',(cnt[0][0][0],cnt[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,1,(100,170,0),1)
        
    else:
        print ("star")
        cv2.drawContours(img,[cnt],0,(0,127,255),-1)
        cv2.putText(img,'star',(cnt[0][0][0],cnt[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,1,(100,170,0),1)
##    elif len(approx) == 9:
##        print "half-circle"
##        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
##    elif len(approx) > 15:
##        print "circle"
##        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
