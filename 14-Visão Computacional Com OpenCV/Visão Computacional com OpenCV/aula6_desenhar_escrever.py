import cv2 
import numpy as np 

#Cores -> BGR ee não RGB
azul = 255,0,0
verde = 0,255,0 
vermelho = 0,0,255


#1 - blanck image
blank_img = np.zeros((500,500,3), dtype='uint8')
cv2.imshow('blank', blank_img)
#2 pintar de vermelho

# blank_img[:] = vermelho 
# cv2.imshow('blank -> vermelho', blank_img)

#3 criando outra em azul


# blank_img[:] = azul
# cv2.imshow('blank -> azul', blank_img)



#4 criando outra em verde


# blank_img[:] = verde
# cv2.imshow('blank -> verde', blank_img)


#5 vamos pintar uma parte específica


# blank_img[200:300, 300:400] = vermelho
# blank_img[:100, 50:150] = verde
# blank_img[400:, 200:300] = azul
# cv2.imshow('blank -> parte especifica vermelha, verde e azul', blank_img)

# 6 desenhando um ratangulo verde 

# cv2.rectangle(blank_img,(10,10),(250,250), verde, -1)
# cv2.imshow('retangulo', blank_img)


# 7  desenhando um ratangulo verde sem ser cheio

# cv2.rectangle(blank_img,(10,10),(250,250), verde, 10)
# cv2.imshow('bordas de um retangulo', blank_img)


# 8  desenhando um ratangulo verde de 30,30 ao  centro

# cv2.rectangle(blank_img,(30,30),(blank_img.shape[1]//2,blank_img.shape[0]//2), verde, 3)
# cv2.imshow('retangulo de 30,30  até o  centro', blank_img)


# 9  desenhando um  círculo
# cv2.circle(blank_img, (blank_img.shape[1]//2,blank_img.shape[0]//2), 200, azul, 5)
# cv2.imshow('Círculo', blank_img)

# # 10  desenhando uma linha
# cv2.line(blank_img,(100,100), (blank_img.shape[1]//2,blank_img.shape[0]//2), azul, 5)
# cv2.imshow('Linha', blank_img)

# 11 Escrevendo texto
cv2.putText(blank_img, "Luiz Academy", (3,250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
cv2.imshow('Texto', blank_img)




cv2.waitKey(0)