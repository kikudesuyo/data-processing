import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
path = glob.glob('/Users/ishidayuichirou/Documents/学生衛星/eisei/Images/*.jpg')
hsv_min = np.array([54, 100, 0])#多分この値が限界これ以上間を小さくするとオーロラの画像を間違える
hsv_max = np.array([60, 255, 255])
list_max = []#それぞれ画像のの緑色のピクセルの数を収納するリスト
list_min = []#それぞれ画像の緑色以外のピクセルの数を収納するリスト
list_hist = []#ヒストグラムを書くためのリスト
list_percent = []#それぞれの画像の緑色のピクセルと緑色以外のピクセルの比（パーセント）を格納するリスト
image_divide = 32 #画像の一辺を何分の1にするか
for i in range(len(path)):
    img = cv2.imread(path[i])
    height = img.shape[0]
    width = img.shape[1]
    resized_img = cv2.resize(img,(round(width/image_divide), round(height/image_divide)))
    resized_img_HSV = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
    maskHSV = cv2.inRange(resized_img_HSV,hsv_min,hsv_max)
    resultHSV = cv2.bitwise_and(resized_img, resized_img, mask = maskHSV)
    img_hist, img_bins = np.histogram(np.array(maskHSV).flatten(), bins=np.arange(256+1))
    img_hist_np = np.array(img_hist)
    list_hist.append(img_hist_np)
    number_of_max = int(img_hist[255])#緑のピクセルの量
    list_max.append(number_of_max)
    number_of_min = int(img_hist[0])#緑以外のピクセルの量
    list_min.append(number_of_min)
    percent_green = number_of_max/number_of_min #緑とそれ以外のピクセルの割合
    list_percent.append(percent_green)
print(list_max)#それぞれ画像のの緑色のピクセルの数を収納するリストを出力
print(list_min)#それぞれ画像の緑色以外のピクセルの数を収納するリストを出力
print(list_percent)#それぞれの画像の緑色のピクセルと緑色以外のピクセルの比（パーセント）を格納するリストを出力
for i in range(len(list_hist)):
    plt.subplot(5, 2, i+1)
    plt.title(label=str(i))
    plt.plot(list_hist[i])
#plt.savefig("img_hist.png")
plt.show()

path = glob.glob('/Users/ishidayuichirou/Documents/学生衛星/eisei/Images/earth/*.jpg')
list_max_earth = []#それぞれ画像のの緑色のピクセルの数を収納するリスト
list_min_earth = []#それぞれ画像の緑色以外のピクセルの数を収納するリスト
list_hist = []#ヒストグラムを書くためのリスト
list_percent_earth = []#それぞれの画像の緑色のピクセルと緑色以外のピクセルの比（パーセント）を格納するリスト
for i in range(len(path)):
    img = cv2.imread(path[i])
    height = img.shape[0]
    width = img.shape[1]
    resized_img = cv2.resize(img,(round(width/image_divide), round(height/image_divide)))
    resized_img_HSV = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
    maskHSV = cv2.inRange(resized_img_HSV,hsv_min,hsv_max)
    resultHSV = cv2.bitwise_and(resized_img, resized_img, mask = maskHSV)
    img_hist, img_bins = np.histogram(np.array(maskHSV).flatten(), bins=np.arange(256+1))
    img_hist_np = np.array(img_hist)
    list_hist.append(img_hist_np)
    number_of_max = int(img_hist[255])#緑のピクセルの量
    list_max_earth.append(number_of_max)
    number_of_min = int(img_hist[0])#緑以外のピクセルの量
    list_min_earth.append(number_of_min)
    percent_green = number_of_max/number_of_min #緑とそれ以外のピクセルの割合
    list_percent_earth.append(percent_green)
print(list_max_earth)#それぞれ画像のの緑色のピクセルの数を収納するリストを出力
print(list_min_earth)#それぞれ画像の緑色以外のピクセルの数を収納するリストを出力
print(list_percent_earth)#それぞれの画像の緑色のピクセルと緑色以外のピクセルの比（パーセント）を格納するリストを出力
for i in range(len(list_hist)):
    plt.subplot(5, 2, i+1)
    plt.title(label=str(i))
    plt.plot(list_hist[i])
#plt.savefig("img_hist_earth.png")
plt.show()

threshold = 0.01 #オーロラとオーロラ以外の画像を判別するための閾値を設定、これをlist_percentの要素に当てはめる
predict_aurora = []#閾値からオーロラを判断できるかどうか。オーロラと判断すると1, そうでないと0とする
predict_else = []#閾値からオーロラ以外と判断できるかどうか

#閾値からオーロラを判断できるかどうか
for i in range(len(list_percent)):
    x = list_percent[i]
    if x > threshold:
        predict_aurora.append(1)
    else:
        predict_aurora.append(0)
#閾値からオーロラ以外と判断できるかどうか
for i in range(len(list_percent_earth)):
    x = list_percent_earth[i]
    if x > threshold:
        predict_else.append(1)
    else:
        predict_else.append(0)
print(predict_aurora)
print(predict_else)

#予測結果から混同行列を計算する
predict_aurora = np.array(predict_aurora)
answer_aurora = np.ones_like(predict_aurora)
predict_else = np.array(predict_else)
answer_else = np.zeros_like(predict_else)
predict = np.concatenate([predict_aurora, predict_else])
answer = np.concatenate([answer_aurora, answer_else])
from sklearn.metrics import confusion_matrix
c_matrix = confusion_matrix(answer, predict)
print(c_matrix)

#予測結果からAUROCを計算する
from sklearn.metrics import roc_auc_score
AUROC = roc_auc_score(predict, answer)
print(AUROC)