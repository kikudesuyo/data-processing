import cv2
import numpy as np
import math
#画像読込、表示、保存
filename = 'orora.jpg'
img_raw=cv2.imread(filename)
cv2.imshow('Img',img_raw)
cv2.waitKey()
img_raw_h = img_raw.shape[0]
img_raw_w = img_raw.shape[1]
img_h = math.floor((img_raw_h/2))
img_w = math.floor((img_raw_w/2))
img = np.zeros((img_h, img_w) ,np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# zerosであると白黒になるがcvtcolorを使うことで色が使える
y = 0
while y < img_raw_h -2:
    x = 0
    while x < img_raw_w -2:
        rgb = [0, 0, 0]
        for z in range(3):
            # 255を超えないように1/4したものを足した(原因はよくわからない)
            rgb[z] = math.floor((img_raw[x,y][z]/4+ img_raw[x,y+1][z]/4+ img_raw[x+1,y][z]/4 + img_raw[x+1,y+1][z]/4))
        img[math.floor(x/2), math.floor(y/2)] = (rgb[0], rgb[1], rgb[2])
        x += 2
    y += 2

cv2.imshow('Img', img)
# 出力されるファイル名を作成
new_name = filename.split('.')[0]
extension = filename.split('.')[-1]
new_filename = ""
if str.isdigit(new_name[-1]):
    new_filename = new_name[0:-1]+str(int(new_name[-1])+1)+'.'+extension
else:
    new_filename = new_name+'2.'+extension
cv2.imwrite(new_filename, img)
cv2.waitKey()


# 画像が正方形のみ対応可能
#長方形であると長いほうが余っておかしくなるかも
# png かjpgで圧縮率が異なったがどちらを採用するか？
# 画素数を1/4にしても容量が1/4にならなかった

