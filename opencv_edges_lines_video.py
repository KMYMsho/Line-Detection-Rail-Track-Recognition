import numpy as np
import cv2
import functions as fnc

cap = cv2.VideoCapture('railroad_video1.mp4')

div = 1
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/div)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/div)
print(width, height)

choose_frame = "default" # default, blur, lines
key = "lines" # edges or lines
tp = "g" # g, m, gm, or mg 
value = 5

#try while(cap.isOpened()):
#ret1, frame1 = cap.read()
#ret2, frame2 = cap.read()
#To display multiple frames without overwriting

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
    	break
    lines = fnc.find_lines_GaussianBlur(frame, value)
    cv2.imshow("Gaussian Blur", lines)

    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break
    # if key == "edges":
    #   if tp == "g":
    #     edges = fnc.g_edges(frame, g_value)
    #     cv2.imshow("g_edges", edges)
    #   elif tp == "m":
    #     edges = fnc.m_edges(frame, m_value)
    #     cv2.imshow("m_edges", edges)
    #   elif tp == "gm":
    #     edges = fnc.gm_edges(frame, g_value, m_value)
    #     cv2.imshow("gm_edges", edgse)
    #   elif tp == "mg":
    #     edges == fnc.mg_edges(frame, m_value, g_value)
    #     cv2.imshow("gm_edges", edges)
    #   else:
    #     print("no match found")
    #     print("input options:")
    #     print("key (edges or lines)")
    #     print("tp (m, g, gm, or mg)")
    #     break

    # elif key == "lines":
    #   if tp == "m":
    #     lines = fnc.find_lines_MedianBlur(frame, m_value)
    #     cv2.imshow("g_lines", lines)
    #   elif tp == "g":
    #     lines, v = fnc.find_lines_GaussianBlur(frame, g_value)
    #     cv2.imshow("m_lines", lines)
    #     print(v)
    #   elif tp == "gm":
    #     lines = fnc.find_lines_gm(frame, g_value, m_value)
    #     cv2.imshow("gm_lines", lines)
    #   elif tp == "mg":
    #     lines = fnc.find_lines_mg(frame, m_value, g_value)
    #     cv2.imshow("mg_lines", lines)
    #   else:
    #     print("no match found")
    #     print("input options:")
    #     print("key (edges or lines)")
    #     print("tp (m, g, gm, or mg)")
    #     break
    # else:
    #   print("no match found")
    #   break

    # if cv2.waitKey(25) & 0xFF == ord('q'): 
    #   break

cap.release()
cv2.destroyAllWindows()
