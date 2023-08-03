import cv2
import numpy as np
#读取图片
image =cv2.imread("poker.jpg")

#转为灰度图
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
template =gray[75:105, 235:265] #方块
h,w=template.shape[:2]

#指定阈值 越大越匹配
threshold=0.9  

#归一化方法比较 返回的是结果值 越大越匹配
res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

#筛选大于阈值的结果值
loc=np.where(res >= threshold)


#画图
for pt in zip(*loc[::-1]):
    bottom=(pt[0]+w, pt[1]+h)
    cv2.rectangle(image,pt,bottom,(0,0,255),2)
    
cv2.imshow("image",image)

cv2.waitKey()