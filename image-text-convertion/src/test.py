from telnetlib import WILL
import PIL
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image
#画像読込、表示、保存
filename_before = '../img/orora-comp.png'
img_before = Image.open(filename_before)
filename_after = '../img/orora-recovered.png'
img_after = Image.open(filename_after)

is_equal = True
for y in range(img_before.height):
    for x in range(img_before.width):
        is_equal = img_before.getpixel((x,y))[:4] == img_after.getpixel((x,y))[:4]
        if is_equal == False:
            print('before',img_before.getpixel((x,y))[:4])
            print('after',img_after.getpixel((x,y))[:4])

