import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
#画像読込、表示、保存
img_raw = cv2.imread('../img/orora-compressed.jpg')
cv2.imshow('Img',img_raw)
cv2.waitKey()
img_raw_h = img_raw.shape[0]
img_raw_w = img_raw.shape[1]
img_h = math.floor((img_raw_h/4))
img_w = math.floor((img_raw_w/4))
img = np.zeros((img_h, img_w) ,np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

y = 0
while y < img_raw_h-4:
    x = 0
    while x < img_raw_w-4:
        rgb = [0, 0, 0]
        for z in range(3):
                                 # 255を超えないように1/16したものを足した。
                                 # 以上の処理は、画素の平均を取っている(ピークとノイズについて改善の余地あり)
            rgb[z] = math.floor((img_raw[x,y][z]/16+ img_raw[x,y+1][z]/16 + img_raw[x,y+2][z]/16 + img_raw[x,y+3][z]/16 + 
                                 img_raw[x+1,y][z]/16+ img_raw[x+1,y+1][z]/16 + img_raw[x+1,y+2][z]/16 + img_raw[x+1,y+3][z]/16 +
                                 img_raw[x+2,y][z]/16+ img_raw[x+2,y+1][z]/16 + img_raw[x+2,y+2][z]/16 + img_raw[x+2,y+3][z]/16 +
                                 img_raw[x+3,y][z]/16+ img_raw[x+3,y+1][z]/16 + img_raw[x+3,y+2][z]/16 + img_raw[x+3,y+3][z]/16))
                                
        img[math.floor(x/4), math.floor(y/4)] = (rgb[0], rgb[1], rgb[2])
        x += 4
    y += 4
cv2.imshow('Img', img)
cv2.imwrite('../img/orora-compressed.jpg', img)
cv2.waitKey()

# png とjpgでは圧縮率が異なっていた、どちらにするか？？