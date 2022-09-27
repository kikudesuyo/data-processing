from telnetlib import WILL
import PIL
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image
#画像読込、表示、保存
filename = '../img/orora-comp.png'
img = Image.open(filename)

# 分割
pixels_with_header = []

parts = ""
count = 0   
i = 1
for y in range(img.height):
    for x in range(img.width):
        rgb_deci = img.getpixel((x,y))[:3]
        # 右端の画素のヘッダーに1、それ以外は0
        rgb_hexa = '1' if x == img.width-1 else '0' #怪しいよ
        # # rgbを16進数に変換
        for color in rgb_deci:
            hexa = hex(color)[2:]
            # 2桁に揃える
            if len(hexa) == 2:
                rgb_hexa += hexa
            else:
                rgb_hexa += '0' + hexa
            count += 1
        parts += rgb_hexa
        #100バイト程度に分割
        if count % 25 == 0 or (x == img.width-1 and y == img.height-1):
            # pixels_with_header.append(parts) #再結合に使用
            filename = '../temp/part' + str(i) + '.txt'
            f = open(filename, 'w')
            f.write(parts)
            i += 1
            parts = ""