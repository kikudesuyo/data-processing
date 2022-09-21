from telnetlib import WILL
import PIL
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image
#画像読込、表示、保存
filename = 'gravity-wave.jpg'
img = Image.open(filename)

# 分割
pixels_with_header = []
parts = []
count = 0
for y in range(img.height):
    for x in range(img.width):
        rgb_deci = img.getpixel((x,y))
        # 右端の画素のヘッダーに1、それ以外は0
        rgb_hexa = '1' if x == img.width-1 else '0'
        # rgbを16進数に変換
        for color in rgb_deci:
            hexa = hex(color)[2:]
            rgb_hexa += hexa if len(hexa) == 2 else '0' + hexa
        count += 1
        parts.append(rgb_hexa)
        #100バイト程度に分割
        if count % 25 == 0 or (x == img.width-1 and y == img.height-1):
            pixels_with_header.append(parts)
            parts = []

            
#再結合
w = 0
h = 0
pixels = []
row = []
for parts in pixels_with_header:
    for rgb_str in parts:
        # ['01d3123']→(31,49,35)に変換
        rgb = tuple([int(rgb_str[i: i+2],16) for i in range(1, len(rgb_str), 2)])  
        row.append(rgb)
        if h == 0:
            w += 1
        if rgb_str[0] == '1':
            h += 1
            pixels.append(row)
            row = []
size = (w,h)
rgb_color = (0,0,0)
new_img = Image.new('RGB', size, rgb_color)
for y in range(h):
    for x in range(w):
        new_img.putpixel(((x,y)), pixels[y][x])
new_img.show()
new_img.save('recovered_gravity-wave.png')


    




            
            
            
            

        

            
        


        
        
            
            
            
            
            
            
            
            
          
            
