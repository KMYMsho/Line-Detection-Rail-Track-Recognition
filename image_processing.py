import cv2
import numpy as np
import functions as fnc
import matplotlib.pyplot as plt 

# value = 5 
# cols = 5 
# rows = 1
# image = cv2.imread("railroad_image_2.jpg")
# img = cv2.imread("railroad_image_2.jpg")
# gray, blur, edge, line = fnc.return_everything(img, 5)

# l = [image, gray, blur, edge, line]
# l_str = ["Original", "GRAY", "BLUR", "EDGE", "LINE"]

# fig = plt.figure(figsize=(10, 5))
# for i in range(1, len(l)+1):
#     fig.add_subplot(rows, cols, i).set_title(l_str[i-1], fontsize=14)
#     plt.imshow(l[i-1])
# plt.show()
source="railroad_img.jfif"
image = cv2.imread(source)
img = cv2.imread(source)
gray, blur, edge, line = fnc.return_everything(img, 9)
cv2.imshow("original", image)
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("edge", edge)
cv2.imshow("line", line)
cv2.waitKey(500000) 
cv2.destroyAllWindows()