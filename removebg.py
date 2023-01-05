from rembg import remove
from PIL import Image
if __name__ == '__main__':
    img = Image.open("C:/Users/HP/Desktop/python/background/matteformer-master/data/image/dog.png")
    output = remove(img)
    output.save('asdfasdf.png')