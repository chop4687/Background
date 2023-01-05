from PIL import Image
import numpy as np
if __name__ == '__main__':
    img = Image.open("C:/Users/HP/Desktop/python/background/duex.png").convert('RGBA')
    arr_img = np.array(img)

    r, g, b = arr_img[...,0], arr_img[...,1], arr_img[...,2]
    idx1 = np.where(g > 100, 0, 255)
    idx2 = np.where(g < 210, 0, 255)
    idx3 = np.where(r < 120, 0, 255)
    idx4 = np.where(b < 120, 0, 255)
    idx = idx1+idx2+idx3+idx4
    print(np.unique(idx))
    idx_f = np.where(idx == 0, 0, 255)
    print(idx_f)
    arr_img[...,3] = idx_f
    output = Image.fromarray(arr_img)
    output.save('asdfasdf.png')
