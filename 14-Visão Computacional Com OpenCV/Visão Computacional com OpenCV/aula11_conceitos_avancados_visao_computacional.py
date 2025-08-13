import cv2 
import numpy as np


def show_img(titulo, image):
    cv2.imshow(titulo, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('OpenCV/assets/fotos/cat.jpg')
#show_img("Imagem padrão", img)

average = cv2.blur(img, (6,6))
#show_img('Blur por média', average)

gauss = cv2.GaussianBlur(img, (7,7), 0)
#show_img('Gaussian Blur', gauss)


median = cv2.medianBlur(img,9)
#show_img("Median Blur", median)

img_noisy = cv2.imread("OpenCV/assets/fotos/noisy_image.jpg")
show_img('Imagem com ruido', img_noisy)

bilateral = cv2.bilateralFilter(img_noisy,15,75,75)
show_img('Filtro Bilateral', bilateral)


