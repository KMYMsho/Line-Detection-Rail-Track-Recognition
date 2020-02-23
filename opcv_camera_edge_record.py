import numpy as np
import cv2
import functions as fnc 

cap = cv2.VideoCapture(0)
div = 1
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/div)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/div)
print(width, height)
fps = 20.0
dim = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test_record_4.mp4v', fourcc, fps, dim)
value = 9

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
      break
    lines = fnc.find_lines_GaussianBlur(frame, value)
    out.write(lines)
    cv2.imshow("Gaussian Blur", lines)

    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break


cap.release()
cv2.destroyAllWindows()
