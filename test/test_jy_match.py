import cv2
import numpy as np

#读取两张图片
image = cv2.imread("OIP.jfif")
image1 =cv2.imread("OIPcross.jfif")
#转为灰度图
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# 使用 SIFT 或 SURF 算法提取图片的特征点和特征描述符
sift=cv2.SIFT_create()
kp1, des1=sift.detectAndCompute(gray,None)
kp1, des2=sift.detectAndCompute(gray1,None)

# 使用 FLANN 或 Brute-Force 算法进行特征匹配
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)


# 绘制匹配的结果并输出到文档中
doc = open("matches.txt", "w")
doc.write("Number of matches: " + str(len(matches)) + "\n\n")
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        doc.write(str(m.queryIdx) + " " + str(m.trainIdx) + " " + str(m.distance) + "\n")
doc.close()


cv2.imshow("OIP",image)
cv2.waitKey()