import cv2 
import numpy as np

img = cv2.imread('OpenCV/assets/fotos/cats.jpg')
#cv2.imshow('CATS', img)

blank = np.zeros(img.shape[:2], dtype="uint8")
#cv2.imshow('Blank', blank)

#criar formas

circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1 )
rectangle = cv2.rectangle(blank.copy(),(30,30),(370,370), 255, -1)
# cv2.imshow('circulo',circle)
# cv2.imshow('retangulo',rectangle)

#Criando máscaras diferentes

recorte1 = cv2.bitwise_and(circle, rectangle) 
recorte2 = cv2.bitwise_or(circle, rectangle) 
recorte3 = cv2.bitwise_not(circle) 

# cv2.imshow('recorte1 circle AND rectangle',recorte1)
# cv2.imshow('recorte2 circle OR rectangle',recorte2)
# cv2.imshow('recorte3 NOT CIRCLE',recorte3)


#mostrando as máscaras

mask1 = cv2.bitwise_and(img, img, mask=recorte1)
mask2 = cv2.bitwise_and(img, img, mask=recorte2)
mask3 = cv2.bitwise_and(img, img, mask=recorte3)

# cv2.imshow('mascara1', mask1)
# cv2.imshow('mascara2', mask2)
# cv2.imshow('mascara3', mask3)


cv2.waitKey(0)