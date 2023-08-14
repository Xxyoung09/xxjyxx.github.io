from PIL import ImageGrab

# 指定截图区域的坐标
left = 500
top = 500
right = 1000
bottom =1000

# 获取屏幕截图
screenshot = ImageGrab.grab(bbox=(left,top,right,bottom))

# 显示截图
screenshot.show()

# 保存截图
screenshot.save("screenshot.png")
