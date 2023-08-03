
import cv2

gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)#直接读取灰度图

laplacian = cv2.Laplacian(gray, cv2.CV_64F) #拉普拉斯算子梯度变化
canny = cv2.Canny(gray, 50, 100)#100-200判断为边缘

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)

cv2.waitKey()

