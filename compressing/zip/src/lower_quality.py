# import zipfile
# zip_f = zipfile.ZipFile('../temp/sample.zip', 'w')
# # i = 0
# # filename = "sample" + str(i) + ".txt"

# zip_f.write("../../split/img/gravity-wave.jpg", compress_type=zipfile.ZIP_DEFLATED)

# zip_f.close()

import cv2

im = cv2.imread('../../split/img/')

for i in range(80, 0, -20):
    cv2.imwrite('/pressure/img/quality' + str(i) + '.jpg', im, [int(cv2.IMWRITE_JPEG_QUALITY), i])
