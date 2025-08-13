import cv2
import numpy as np

cap = cv2.VideoCapture("OpenCV/assets/videos/dog.mp4")

# Criar função que faz o rescale para cada frame individual
def rescale_frame(frame: np.array,
                  scale: float = 0.75,
                  ):
    largura = int(frame.shape[1]*scale)
    altura = int(frame.shape[0]*scale)
    
    return cv2.resize(frame, (largura, altura), interpolation=cv2.INTER_AREA)

def resize_frame(width:int,
                 height:int):
    #somente valido para livevideo
    # 3 - setar width
    # 4 - setar height
    
    cap.set(3, width) 
    cap.set(4, height) 
    
# IMAGEM ========================

# img = cv2.imread("OpenCV/assets/fotos/cat.jpg")
# cv2.imshow('original image', img)

# resized_img = rescale_frame(img, 0.2)
# cv2.imshow('resized image', resized_img)
# cv2.waitKey(0)

# LIVEVIDEO ==============

while True:
    _, frame = cap.read()
    frame_resized = rescale_frame(frame, 0.5)
    cv2.imshow('dog', frame_resized)
    
     
      
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
    
     
    