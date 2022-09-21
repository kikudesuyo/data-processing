import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("iss029e007455~orig.jpg")


"""
img_hist, img_bins = np.histogram(np.array(img).flatten(), bins=np.arange(256+1))
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
# hist 表示
plt.plot(img_hist)
plt.show()
"""


"""
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Color Image')
plt.show()
"""
# 2値化の作成

"""
#1 青の範囲をnp.arrayにて指定
hsv_min = np.array([100,45,70])
hsv_max = np.array([105,255,255])
"""

"""
#1 赤の範囲をnp.arrayにて指定
hsv_min = np.array([0, 64, 0])
hsv_max = np.array([30, 255, 255])
"""


#1 緑の範囲をnp.arrayにて指定
hsv_min = np.array([30, 64, 0])
hsv_max = np.array([90, 255, 255])


#2 取得画像のサイズを変更
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img,(round(width/4), round(height/4)))


#3 画像のHSV化
resized_img_HSV = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

#4 画像の青を白、青以外黒にする
maskHSV = cv2.inRange(resized_img_HSV,hsv_min,hsv_max)

#5青以外マスク
resultHSV = cv2.bitwise_and(resized_img, resized_img, mask = maskHSV)


#cv2.imshow("Result HSV", resultHSV)
#cv2.imshow("Result mask", maskHSV)

#cv2.imshow("Result mask", resized_img_HSV)
#cv2.waitKey(0)
img_hist, img_bins = np.histogram(np.array(maskHSV).flatten(), bins=np.arange(256+1))
plt.plot(img_hist)
cv2.imshow("Result mask", maskHSV)
plt.savefig("hist_1.png")
plt.show()

img_hist2, img_bins2 = np.histogram(np.array(resized_img).flatten(), bins=np.arange(256+1))
plt.plot(img_hist2)
cv2.imshow("Row img", resized_img)
plt.show()


cv2.destroyAllWindows()