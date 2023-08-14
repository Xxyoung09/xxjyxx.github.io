import cv2
import numpy as np

ref_pic=cv2.imread('')
vc=cv2.VideoCapture('')

while True:
    flag,frame =vc.read()
    if not flag:
        break

    frame  =cv2.resize(frame,(ref_pic.shape[1],ref_pic.shape[0]))
    
    gray_ref_pic=cv2.cvtColor(ref_pic,cv2.COLOR_BGR2GRAY)
    gray_frame  =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 