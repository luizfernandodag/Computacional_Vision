import cv2
import numpy as np 

img = cv2.imread("OpenCV/assets/fotos/cat.jpg")
img2 = cv2.imread("OpenCV/assets/fotos/park.jpg")

#1. Converter pra P&B (greyscale)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gatinho', img)
#cv2.imshow('gatinho cinza', cinza)

# 2. Blur

blurred = cv2.GaussianBlur(img,(3,3), cv2.BORDER_DEFAULT)
#cv2.imshow('blurred', blurred)


# 3. Edge Cascade - detecção de borda - detecção de descontinuidade no brilho


canny = cv2.Canny(img, 250, 200)
#cv2.imshow('canny1', canny)


# 4 Edge detecion com imagem blured
canny_blurred = cv2.Canny(blurred, 250,200)
#cv2.imshow('canny blurred', canny_blurred)

# 5 Dilatação de Imagem - aumentar tamnho e espessura de um objeto numa imagem

dilated = cv2.dilate(canny_blurred, (9,9), iterations=3)
#cv2.imshow('dilatada', dilated)

# 6  Eroding Image - Corroendo Imagem

eroded = cv2.erode(dilated,(9,9), iterations=3)
#cv2.imshow('eroded', eroded)

# 7 Resize

resized = cv2.resize(img, (300,300))
#cv2.imshow('resized',resized)

# 8 Crop

corte = img[50:200,200:400]
cv2.imshow('corte de matriz', corte)

#9 ér possível fazer operações direto no imshow()

cv2.imshow('corte de direto', img[50:200, 200:400] )




cv2.waitKey(0)