import cv2 
import numpy as np



img = cv2.imread('OpenCV/assets/fotos/park.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem em cinza', gray)

# MÉTODO LAPLACIANO
# cv2.Laplacian(imagem, data_depth)

laplaciano = cv2.Laplacian(gray,cv2.CV_64F)
#print(laplaciano)

#calcular o valor absoluto por elemento e converter para uint8(0 a 255)
laplaciano = np.uint8(np.absolute(laplaciano))
#print()
#print(laplaciano)

cv2.imshow("Laplaciano refatorado", laplaciano)

#Método de SOBEL -> gradiente da quantidade luz -> maior variação
# cv2.Sobel(imagem, ddepth, dx, dy) onde dx e dy representam as direções x e y
x = cv2.Sobel(gray, cv2.CV_64F, 1,0)
y = cv2.Sobel(gray, cv2.CV_64F, 0,1)

#resultados separados das derivadas com o método de Sobel
#cv2.imshow('SOBEL X',x)
#cv2.imshow('SOBEL Y',y)

#combinar x e y em uma bitwise operation or

combined_sobel = cv2.bitwise_or(x,y)
#cv2.imshow('Sobel combinado x+y', combined_sobel)

#MÉTODO DE CANNY
canny = cv2.Canny(gray, 150, 175)
cv2.imshow("Filtro Canny", canny)












cv2.waitKey(0)