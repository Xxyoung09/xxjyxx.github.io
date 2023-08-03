
import cv2
import numpy as np

image = cv2.imread("poker.jpg")   #读图片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #转为灰度图

template  = gray[75:105, 235:265] #方块
template1 = gray[66:100, 364:385] #黑桃

match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
match1 = cv2.matchTemplate(gray,template1,cv2.TM_CCOEFF_NORMED)


locations = np.where(match >= 0.9)
locations1 =np.where(match1 >= 0.9)


w, h = template.shape[0:2]
w1,h1 =template1.shape[0:2]

for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

for p1 in zip(*locations1[::-1]):
    x1, y1 = p1[0], p1[1]
    x2, y2 = x1 + w1, y1 + h1
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 255), 2)

cv2.imshow("image", image)
#cv2.imshow("gray",gray)
cv2.waitKey()


