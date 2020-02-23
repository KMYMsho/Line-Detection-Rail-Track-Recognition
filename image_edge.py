import numpy as np
import cv2
import functions as fnc 

frame = cv2.imread("railphoto2.jpg")
value = 13
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (value, value), 0)
edges = fnc.auto_canny(blur)
cv2.imshow("edges", edges)
result = cv2.imwrite('railphoto_edges.jpg', edges)
cv2.waitKey(0) 
cv2.destroyAllWindows() 