import numpy as np
import os
import imageio
import OpenEXR
import Imath
from PIL import Image
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2

if __name__ == '__main__':
    path_dir = "D:/DANCE/"
    for k in os.listdir(path_dir):
        path = path_dir+k+"/plate/v01"
        #path = 'C:/Users/HP/Desktop/python/background/DANCE/v01'

        dir = os.listdir(path)

        for i in dir:
            file_name = os.path.join(path,i)
            img = cv2.imread(file_name,cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
            img=img*255
            img[img>255]=255
            img=np.uint64(img)
            cv2.imwrite('./DANCE/sample_png/'+i[:-4]+'.png',img)
            print(i)
        