import cv2
import numpy as np

# 读取图片
image = cv2.imread("/home/jy/opencv/pic/poker.jpg")

# 转为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 读取目标模板
template = gray[75:105, 235:265]  # 方块
h, w = template.shape[:2]

# 设置阈值
threshold = 0.9

# 使用归一化方法比较，计算匹配结果
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

# 筛选出匹配结果大于阈值的位置
loc = np.where(res >= threshold)

# 保存匹配结果到文件
with open("matches.txt", "w") as f:
    for pt in zip(*loc[::-1]):
        f.write(f"{pt[0]}, {pt[1]}\n")

        # 在图像上标注匹配位置
        bottom = (pt[0] + w, pt[1] + h)
        cv2.rectangle(image, pt, bottom, (0, 0, 255), 2)


# 输出匹配结果文件
with open("matches.txt", "r") as f:
    print(f.read())
    
# 显示带标注的图像
cv2.imshow("image", image)
cv2.waitKey()