import cv2
import numpy as np
from PIL import ImageGrab



# 图像对比函数
def compare_images(image1, image2):



    #width1,height1=image1.size
    #width2,height2=image2.size
    
    np_image1=np.array(image1)
    np_image2=np.array(image2)
    #确保两个图像具有相同的尺寸
    #if width1==width2 and height1==height2:
    if np_image1.shape== np_image2.shape:
        # 逐像素比较两个图像
        difference = cv2.subtract(np_image1, np_image2)
        b, g, r = cv2.split(difference)

        # 将差异图像转换为灰度图像
        gray_diff = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

        # 阈值化灰度图像，将非零像素设置为255
        _, threshold = cv2.threshold(gray_diff, 0, 255, cv2.THRESH_BINARY)

        # 统计非零像素的数量
        num_diff_pixels = cv2.countNonZero(threshold)

        if num_diff_pixels == 0:
            print("两个图像完全相同")
        else:
            print("两个图像不完全相同")
    else:
        print("两个图像尺寸不同")


if __name__ == "__main__":
    # 指定截图区域的坐标
    left = 500
    top =  500
    right =  1000
    bottom = 1000
    #截屏次数
    num_screenshot=5
    # 图像对比
    tem_image = cv2.imread('/home/jy/opencv/pic/cross.png')
    screenshot = cv2.imread('/home/jy/opencv/screenshot.png')
   
    for i in range(num_screenshot):
        screenshot=ImageGrab.grab(bbox=(left,top,right,bottom))
        screenshot.save("screenshot.png")
        compare_images(tem_image, screenshot)