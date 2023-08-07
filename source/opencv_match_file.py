import cv2
import numpy as np
import os

def find_template_matches(image_path,template_path,threshold,output_file_dir):
    # 读取图片
    image = cv2.imread(image_path)
    image_template= cv2.imread(template_path)

    # 转为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template=cv2.cvtColor(image_template,cv2.COLOR_BGR2GRAY)

    # 读取目标模板
    #x1,y1,x2,y2=template_pos
    #template = gray[y1:y2,x1:x2]
    #template=gray_template
    h, w = gray_template.shape[:2]
    
    # 使用归一化方法比较，计算匹配结果
    res = cv2.matchTemplate(gray, gray_template, cv2.TM_CCOEFF_NORMED)
    
    # 输出文件目录及名字
    output_file=os.path.join(output_file_dir, os.path.basename(image_path)+ ".txt")

    # 筛选出匹配结果大于阈值的位置
    loc = np.where(res >= threshold)

    # 保存匹配结果到文件
    with open(output_file, "w") as f:
        for pt in zip(*loc[::-1]):
            f.write(f"{pt[0]}, {pt[1]}\n")

            # 在图像上标注匹配位置
            bottom = (pt[0] + w, pt[1] + h)
            cv2.rectangle(image, pt, bottom, (0, 0, 255), 2)

    # 输出匹配结果文件
    with open(output_file, "r") as f:
        print(f.read())
                
    # 显示带标注的图像
    cv2.imshow("image", image)
    cv2.waitKey()
    
def batch_find_template_matches(image_dir,template_path,threshold,output_file_dir):
    for image_file in os.listdir(image_dir):
        if not image_file.endswith(".jpg"):
            continue
        image_path = os.path.join(image_dir,image_file)
        #output_file = os.path.splitext(image_file)[0] +".txt"
        #output_file = os.path.join(output_file_dir,os.path.basename(image_path)+".txt")
        find_template_matches(image_path,template_path,threshold,output_file_dir)
        
if __name__ == "__main__":
    image_dir = "/home/jy/opencv/pic/"
    template_path ="/home/jy/opencv/pic/poker_template.jpg"
    threshold = 0.90
    output_file_dir = "/home/jy/opencv/check_result"
    batch_find_template_matches(image_dir,template_path,threshold,output_file_dir)
    #find_template_matches(image_path, template_pos, threshold, output_file)
