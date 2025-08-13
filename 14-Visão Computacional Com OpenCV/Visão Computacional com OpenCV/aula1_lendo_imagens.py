import cv2

#Função imread()
img = cv2.imread("OpenCV/assets/fotos/cat.jpg")
img2 = cv2.imread("OpenCV/assets/fotos/cat_large.jpg")

#Imshow()
#cv2.imshow('Janela do gato', img)
cv2.imshow('Janela do gato grande', img2)

# Função waitkey()
cv2.waitKey(0) # Espara a tecla 0