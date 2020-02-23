import numpy as np
import cv2

def auto_canny(image, sigma=0.33):
  v = np.median(image)
  lower = int(max(0, (1.0 - sigma)*v))
  upper = int(min(255, (1.0 + sigma)*v))
  edged = cv2.Canny(image, lower, upper)
  return edged 


while(cap.isOpened()):
    ret, frame = cap.read()

    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()