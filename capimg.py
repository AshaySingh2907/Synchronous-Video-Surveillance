# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:33:01 2020

@author: Anshi
"""

import cv2
import os

def video_to_frames(path):
    vidcap = cv2.VideoCapture(0)
    count = 0
    while count<1:
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path, 'test.jpg'),image)
            count += 1
            
        cv2.imshow("Color Frame",image)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    vidcap.release()
    cv2.destroyAllWindows()
    

#video_to_frames(r'C:\Users\Anshi\FYP\FACE_REC')