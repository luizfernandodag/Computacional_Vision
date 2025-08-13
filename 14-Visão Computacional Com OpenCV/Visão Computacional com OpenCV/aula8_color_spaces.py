import cv2 
import numpy as np


img = cv2.imread('OpenCV/assets/fotos/cat.jpg')
cv2.imshow('Normal', img)

#BGR para grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Cinza', gray)

# BGR para HSV

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV', hsv)

#BGR para L*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#cv2.imshow('LAB', lab)


#BGR para L*a*b
RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('RGB', RGB)

#LAB para BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('lab para bgr', lab_bgr)





cv2.waitKey(0)
