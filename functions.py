import numpy as np
import cv2

def auto_canny(image, sigma=0.33):
  v = np.median(image)
  lower = int(max(0, (1.0 - sigma)*v))
  upper = int(min(255, (1.0 + sigma)*v))
  edged = cv2.Canny(image, lower, upper)
  return edged

def regular_canny(image):
  return cv2.Canny(image, 100, 200)

def g_edges(frame, value):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (value, value), 0)
  edges = auto_canny(blur)
  return edges  

def m_edges(frame, value):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blur = cv2.medianBlur(gray, value)
  edges = auto_canny(blur)
  return edges

def mg_edges(frame, mb_value, gb_value):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  mblur = cv2.medianBlur(gray, mb_value)
  gblur = cv2.GaussianBlur(mblur, (gb_value, gb_value), 0)
  edges = auto_canny(gblur)
  return edges  

def gm_edges(frame, mb_value, gb_value):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gblur = cv2.GaussianBlur(gray, (gb_value, gb_value), 0)
  mblur = cv2.medianBlur(gblur, mb_value)
  edges = auto_canny(mblur)
  return edges  

def return_everything(image, value):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (value, value), 0)
  edge = auto_canny(blur)
  lines = cv2.HoughLinesP(edge, 1, np.pi/180, 100, minLineLength=100, maxLineGap=2)
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line[0]
      if abs(x2-x1)<20:
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
      else:
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 5)
  return gray, blur, edge, image

def find_lines_GaussianBlur(frame, value):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (value, value), 0)
  edges = auto_canny(blur)

  lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=2)
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line[0]
      # print(x1, y1, x2, y2)
      if abs(x2-x1)<20:
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
      else:
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
  return frame

def find_lines_MedianBlur(frame_m, value):
  gray = cv2.cvtColor(frame_m, cv2.COLOR_BGR2GRAY)
  blur = cv2.medianBlur(gray, value)
  edges = auto_canny(blur)

  lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=10)
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line[0]
      if abs(x2-x1)<15:
        cv2.line(frame_m, (x1, y1), (x2, y2), (0, 255, 0), 5)
      else:
        cv2.line(frame_m, (x1, y1), (x2, y2), (0, 0, 255), 5)
  return frame_m

  lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=10)
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line[0]
      # print(x1, y1, x2, y2)
      if abs(x2-x1)<20:
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
      else:
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
  return frame

def find_lines_gm(frame, mb_value, gb_value):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gblur = cv2.GaussianBlur(gray, (gb_value, gb_value), 0)
  mblur = cv2.medianBlur(gblur, mb_value)
  edges = auto_canny(mblur) 

  lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=2)
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line[0]
      cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)

  return frame

def find_lines_mg(frame, mb_value, gb_value):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  mblur = cv2.medianBlur(gray, mb_value)
  gblur = cv2.GaussianBlur(mblur, (gb_value, gb_value), 0)
  edges = auto_canny(gblur) 

  lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=2)
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line[0]
      cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
  return frame

def region_selection(image):
  mask = np.zeros_like(image)
  if len(image.shape) > 2:
    channel_count = image.shape[2]
    ignore_mask_color = (255,) * channel_count
  else:
    ignore_mask_color = 255

  rows, cols = image.shape[:2]
  bottom_left  = [cols * 0.1, rows * 0.95]
  top_left     = [cols * 0.4, rows * 0.6]
  bottom_right = [cols * 0.9, rows * 0.95]
  top_right    = [cols * 0.6, rows * 0.6]
  vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
  asked_image = cv2.bitwise_and(image, mask)
  return masekd_image