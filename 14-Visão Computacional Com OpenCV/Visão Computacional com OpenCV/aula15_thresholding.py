import cv2 

'''
Thresholding
-Segmentação de Imagem
-A partir de imagens em cinza, criamos imagens binárias
-Melhores Condições
    - Ruído Baixo
    - Pixels de um mesmo grupo têm intensidade mais próximas entre si do que pixels de outro grupo
    - Luz homogênea 
'''

img = cv2.imread('OpenCV/assets/fotos/cats.jpg')
#cv2.imshow('gatitos', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gatitos em tons de cinza', gray)
'''
Para os thresh simples usaremos a função cv2.threshold()
cv2.threshold(imagem, valor_de_thresh, max_val, metodo_de_thresholding)

metodo_de_threholding ->
cv.THRESH_BINARY: focaremos nesses dois
cv.THRESH_BINARY_INV: focaremos nesses dois
cv.THRESH_TRUNC
cv.THRESH_TOZERO
cv.THRESH_TOZERO_INV
]


'''

#threshold simples -> 
# maior sensibilidade aos pixels brancos

#threshold, thresh = cv2.threshold(gray, 10,255, cv2.THRESH_BINARY)
#cv2.imshow('thresholding simples', thresh)

# menor sensibilidade aos pixels brancos

threshold, thresh = cv2.threshold(gray, 150,255, cv2.THRESH_BINARY)
#cv2.imshow('thresholding simples', thresh)


#threshhold invertido

threshold, thresh_inv = cv2.threshold(gray, 150,255, cv2.THRESH_BINARY_INV)
#cv2.imshow('thresholding simples invertido', thresh_inv)

'''
Adaptative Thresholding
cv2.adaptativeThreshold(imagem, valor_maximo, metodo_adaptativo, metodo_thresholding, tamanho_da_vizinhança, constance_C)


metodo_adaptativo
cv2.ADAPTIVE_THRESH_MEAN_C: o valor limite é a média da área da vizinhaça menos a constante C
cv2.ADAPTIVE_THRESH_GAUSSIAN_C: O valor limite é uma soma ponderada gaussiana dos valores da vizinhaça menos a constante C

'''

# Thresholding Adaptativo

#imagem é melhor que seja escala de cinza
adaptive_thresh_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,9)
adaptive_thresh_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,9)
cv2.imshow('adaptative thresh gaussian', adaptive_thresh_gaussian)
cv2.imshow('adaptative thresh mean', adaptive_thresh_mean)


cv2.waitKey(0)
