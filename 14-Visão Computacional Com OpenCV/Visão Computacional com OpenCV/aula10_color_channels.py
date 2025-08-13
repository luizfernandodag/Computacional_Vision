import cv2 
import numpy as np

parque = cv2.imread('OpenCV/assets/fotos/park.jpg')
cv2.imshow('parque', parque)

#tela vazia

blanck = np.zeros(parque.shape[:2], dtype='uint8')
#cv2.imshow('blanck', blanck)

# separando os canais de cores

b,g,r = cv2.split(parque)
# cv2.imshow('Blue', b)
# cv2.imshow('Red', r)
# cv2.imshow('Green', g)

#reintegrando os canais de cor

blue = cv2.merge([b,blanck, blanck])
green = cv2.merge([blanck,g, blanck])
red = cv2.merge([blanck, blanck, r])
#cv2.imshow('Blue', blue)
#cv2.imshow('Red', red)
#cv2.imshow('Green', green)

# vendo o shape da imagem e das cores

# print(parque.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

# reintegrando a imagem

merged = cv2.merge([b, g,r])
cv2.imshow('imagem reintegrada', merged)
print(parque.shape)
print(merged.shape)




cv2.waitKey(0)

