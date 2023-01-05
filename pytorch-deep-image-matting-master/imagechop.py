import os
from PIL import Image, ImageChops
if __name__ == '__main__':
    img = Image.open("C:/Users/HP/Desktop/python/background/pytorch-deep-image-matting-master/result/example/image/duex.png").convert('RGB')
    mask = Image.open("C:/Users/HP/Desktop/python/background/pytorch-deep-image-matting-master/duex.png").convert('RGB')
    mask_img = ImageChops.multiply(img, mask)
    mask_img.save('mask_duex.png')