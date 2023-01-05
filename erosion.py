import os
from PIL import Image
import numpy as np
import cv2

if __name__ == '__main__':
    #img = Image.open("C:/Users/HP/Desktop/python/background/DIS-main/demo_datasets/your_dataset_result/your_dataset/image_000000000.png").convert('L')
    path = "C:/Users/HP/Desktop/python/background/DANCE/Dance_result/sample_png"
    out_path = "C:/Users/HP/Desktop/python/background/DANCE/erosion"
    dir = os.listdir(path)
    for i in dir:
        img = cv2.imread(os.path.join(path,i), cv2.IMREAD_GRAYSCALE)
        print(i)
        M1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        M2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
        ero_img = cv2.erode(img,M1,iterations=1)
        cv2.imwrite(os.path.join(out_path,i),ero_img)
    '''
    p = 0.01
    width1, height1 = img.size
    img = img.resize((int(width1*(1-p)),int(height1*(1-p))))
    width2, height2 = img.size

    right = int(width1*p/2)
    left = int(width1*p/2)
    top = int(height1*p/2)
    bottom = int(height1*p/2)
    new_width = width2 + right + left
    new_height = height2 + top + bottom
    
    result = Image.new(img.mode, (new_width, new_height), (255))
    
    result.paste(img, (left, top))
    result = result.resize((width1, height1))
    
    result.save('sdfsdf.png')
    '''