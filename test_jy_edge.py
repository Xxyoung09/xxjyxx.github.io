import cv2
import numpy as np  

image1=cv2.imread("R.jfif")
image=cv2.imread("R.jfif",cv2.IMREAD_GRAYSCALE)#灰度
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)#阈值二值化处理
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

dramimage=image1.copy()
cv2.drawContours(dramimage,contours,-1,(0,5,225),2)

cnt=contours[0]
print("面积为：",cv2.contourArea(cnt))
 
#cv2.imshow("image",image)
#cv2.imshow("thresh",thresh)
cv2.imshow("dramimage",dramimage)
cv2.waitKey()
