import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("iss029e007455~orig.jpg")
"""img_hist, img_bins = np.histogram(np.array(img).flatten(), bins=np.arange(256+1))
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)# hist 表示
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
#1
hsv_min = np.array([30, 64, 0])
hsv_max = np.array([90, 255, 255])
#2
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img,(round(width/4), round(height/4)))

#3
resized_img_HSV = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
#4
maskHSV = cv2.inRange(resized_img_HSV,hsv_min,hsv_max)
#5
resultHSV = cv2.bitwise_and(resized_img, resized_img, mask = maskHSV)
#cv2.imshow("Result HSV", resultHSV)
#cv2.imshow("Result mask", maskHSV)
#cv2.imshow("Result mask", resized_img_HSV)
#cv2.waitKey()
img_hist, img_bins = np.histogram(np.array(maskHSV).flatten(), bins=np.arange(256+1))
"""
plt.plot(img_hist)
cv2.imshow("Result mask", maskHSV)
plt.savefig("hist.png")
plt.show()
img_hist2, img_bins2 = np.histogram(np.array(resized_img).flatten(), bins=np.arange(256+1))
plt.plot(img_hist2)
cv2.imshow("Row img", resized_img)
plt.savefig("hist2.png")
plt.show()
cv2.destroyAllWindows()
"""
print(img_hist.shape)
print(img_hist[255])
print(img_hist[0])
number_of_max = int(img_hist[255])#緑のピクセルの量
number_of_min = int(img_hist[0])#緑以外のピクセルの量
percent_green = number_of_max/number_of_min #緑とそれ以外のピクセルの割合
print(percent_green)