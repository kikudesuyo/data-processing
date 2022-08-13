import cv2
img = cv2.imread("orora.jpg")
for i in [10,30,50,80]:
    result, encimg = cv2.imencode("img2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), i])
    cv2.imwrite(str(i)+"output.jpg", img)