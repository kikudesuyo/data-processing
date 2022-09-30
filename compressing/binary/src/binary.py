# 作成させたfilenameから文字列を作成
for i in range(4):
    f = open('../../../image-text-convertion/temp/part'+str(i+1)+'.txt','r')
    body = f.read()
    f.close()
# 文字列をバイナリ表示
binary_converted = ' '.join(format(ord(c), 'b') for c in body)
print(len(binary_converted))
# バイナリ表示させた変数をテキストファイルに出力
for i in binary_converted:
    if len(binary_converted) % 25 == 0:
        binary_textfile = '../temp/binary_textfile' +str(i) +'.txt'
        f = open(binary_textfile, 'w')
        f.write(binary_converted)


# f = open("../temp/myfile_binaryfile.dat", "rb")
# f.write(binary_textfile, "wb")
# f.close()

# バイナリ表示させた変数をバイナリーファイルに出力