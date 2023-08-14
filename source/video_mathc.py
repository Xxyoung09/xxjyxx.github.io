import cv2
import numpy as np

# 加载目标图片（模板）
template = cv2.imread('/home/jy/opencv/pic/cross.png', 0)
w, h = template.shape[::-1]

# 打开视频文件
cap = cv2.VideoCapture('/home/jy/opencv/video/cross.mp4')

while(cap.isOpened()):
    flage, frame = cap.read()

    if flage:
        # 转换为灰度图像
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 使用模板匹配查找图像中的相同元素
        res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
        # 显示结果
        cv2.imshow('Detected', frame)

        # 按下'q'键退出
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()