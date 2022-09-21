from PIL import Image, ExifTags
from pprint import pprint

filename = "hanahusa.jpg"
img = Image.open(filename)
dict = img._getexif()
pprint(dict)
tags = ExifTags.TAGS
pprint(tags)
dict = img._getexif()
exif = {}  # 空の辞書を定義
for key, value in dict.items():
    exif[ExifTags.TAGS[key]] = value  # 辞書の値を新たな辞書のキーとしている

pprint(exif)

print(type(exif))

f = open('exif_data00x.txt', 'w') # 書き込みモードで開く
for key,value in sorted(exif.items()):
	f.write(f'{key} {value}\n')
f.close() # ファイルを閉じる


