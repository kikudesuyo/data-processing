from PIL import Image

# 再結合
w = 0
h = 0
pixels = []
row = []
for i in range(4):
    f = open('../temp/part'+str(i+1)+'.txt','r')
    body = f.read()
    f.close()
    for rgb_str in [body[x:x+7] for x in range(0, len(body), 7)]:
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
new_img.save('../img/orora-recovered.png')
