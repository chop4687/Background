#from tkinter import image_names
#from rembg.bg import remove

from PIL import Image
import cv2
if __name__ == '__main__':
    '''
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    input_image = 'lion.png'
    output_image = 'lion_black.png'

    input = Image.open(input_image)
    
    output = remove(input)
    output_black = output.convert('L')
    threshold = 1
    output_black = output_black.point(lambda p: 0 if p < threshold else 127)
    output_black.save(output_image)
    
    input_image = 'lion_black.png'
    output_image = 'lion_binary.png'
    input = Image.open(input_image)
    threshold = 0
    output_black = input.point(lambda p: 255 if p != threshold else 0)
    output_black.save(output_image)
    
    input_image = 'lion.png'
    mask_image = 'lion_binary.png'
    output_image = 'lion_mask.png'
    input = Image.open(input_image)
    input2 = Image.open(mask_image).convert('RGB')
    masked = ImageChops.multiply(input,input2)
    masked.save(output_image)
    '''
    import os
    img_path = "C:/Users/HP/Desktop/python/background/DANCE/sample_png"
    mask_path = "C:/Users/HP/Desktop/python/background/DANCE/erosion"
    dir = os.listdir(img_path)
    for i in dir:
        input_image = os.path.join(img_path,i)
        mask_image = os.path.join(mask_path,i)
        img = cv2.imread(input_image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
        mask = cv2.imread(mask_image, cv2.IMREAD_GRAYSCALE)
        img[:,:,3] = mask

        cv2.imwrite("C:/Users/HP/Desktop/python/background/DANCE/erosion_2/"+i,img)
        print(i)
    '''
    import os
    out_path = "C:/Users/HP/Desktop/python/background/tttt"
    in_path = "C:/Users/HP/Desktop/python/background/DIS-main/demo_datasets/your_dataset"
    dir = os.listdir(in_path)
    for i in dir:
        input_image = os.path.join(in_path,i)
        mask_image = os.path.join(out_path,i)
        img = Image.open(input_image).convert('RGB')
        mask = Image.open(mask_image).convert('L')
        img.putalpha(mask)
        img.save('./ttt/'+i)
        print(i)
    '''