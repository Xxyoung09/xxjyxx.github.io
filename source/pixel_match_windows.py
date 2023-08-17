import cv2
import time
from PIL import ImageGrab
import numpy as np
import logging
#import win32gui

# 图像对比函数
def compare_images(image1, image2,time_stamp):

    np_image1=np.array(image1)
    np_image2=np.array(image2)

    if np_image1.shape== np_image2.shape:
        # 逐像素比较两个图像
        difference = cv2.subtract(np_image1, np_image2)
        b, g, r = cv2.split(difference)

        # 将差异图像转换为灰度图像
        gray_diff = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

        # 阈值化灰度图像，将非零像素设置为255
        _, threshold = cv2.threshold(gray_diff, 0, 255, cv2.THRESH_BINARY)

        # 统计非零像素的数量
        num_pixel =threshold.size
        num_diff_pixels = cv2.countNonZero(threshold)
        num_same_pixels = num_pixel-num_diff_pixels

        if num_diff_pixels == 0:
            logging.basicConfig(filename='image_compare_log',level=logging.INFO)
            logging.info(f"截图时间 {time_stamp}两个图像完全相同，相同的像素个数：{num_same_pixels}")
            print("两个图像完全相同，相同的像素个数：",num_same_pixels)
            #cv2.imwrite("difference.png",difference)
            #cv2.imwrite("gray_diff.png",gray_diff)
        else:
            #cv2.imshow("difference",difference)
            #cv2.imwrite("difference.png",difference)
            gray_diff_name = f"gray_diff_{timestamp}.png"
            gray_diff_path = "test_image/" + gray_diff_name 
            cv2.imwrite(gray_diff_path,gray_diff)
            print("两个图像不完全相同  不同像素数量:{}  相同像素数量为{}".format(num_diff_pixels,num_same_pixels))
            logging.basicConfig(filename='image_compare_log',level=logging.INFO)
            logging.info(f"截图时间：{time_stamp}两个图像不完全相同，不同的像素数量 {num_diff_pixels} 相同的像素个数：{num_same_pixels} ")
            cv2.waitKey(100)

    else:
        print("两个图像尺寸不同  模板尺寸:{}  截图尺寸:{}".format(np_image1.size,np_image2.size))


if __name__ == "__main__":
    #等待时间
    wait_time=0.05
    #指定截图区域的坐标
    left = 13
    top =  388
    right =  653
    bottom = 868
    #窗口截图 已弃用
    #window_name="vwr::CDesktopWin"
    #window_nd=win32gui.FindWindow(window_name,None)
    #x1,y1,x2,y2=win32gui.GetWindowRect(window_nd)
    #rect=(x1,y1,x2,y2)
    rect1=(left,top,right,bottom)
    #截屏次数
    num_screenshot=100
    
    # 图像对比模板
    tem_image = cv2.imread('cross_tem_695.png')
    #screenshot = cv2.imread('/home/jy/opencv/screenshot.png')
   
    for i in range(num_screenshot):
        #时间戳
        timestamp= time.strftime("%Y%m%d%H%M%S",time.localtime())
        #截图命名
        screenshot_filename=f"screenshot_{timestamp}.png"
        #保存路径
        file_path="test_image/"+ screenshot_filename
        screenshot=ImageGrab.grab(bbox=(rect1))
        screenshot.save(file_path)
        #screenshot.save(screenshot_filename)

        #读取截图并对比
        screenshot_check = cv2.imread(file_path)
        #screenshot_check = cv2.imread(screenshot_filename)
        compare_images(screenshot_check,tem_image,timestamp)
        time.sleep(wait_time)
     