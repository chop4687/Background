import os
from PIL import Image 

if __name__ == '__main__':
    input_path = "C:/Users/HP/Desktop/python/background/DANCE/erosion_2"
    output_path = "C:/Users/HP/Desktop/python/background/DANCE/Dance_change_back"
    dir = os.listdir(input_path)
    for i in dir:
        img = Image.open(os.path.join(input_path,i)).convert('RGBA')
        bgr = Image.new('RGBA', img.size, (255, 255, 255,255))
        width = (bgr.width - img.width) // 2
        height = (bgr.height - img.height) // 2
        bgr.paste(img, (width, height), img)
        bgr.save(os.path.join(output_path,i), format="png")
        print(i)
