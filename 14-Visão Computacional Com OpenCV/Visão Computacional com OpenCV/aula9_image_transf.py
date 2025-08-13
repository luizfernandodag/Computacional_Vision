import cv2 
import numpy as np

img = cv2.imread("OpenCV/assets/fotos/park.jpg")
cv2.imshow('',img)


def translate(img, x,y):
    translation_matrix = np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    
    return cv2.warpAffine(img, translation_matrix, dimensions)

def rotate(img, angle, rotation_point = None ):
    height, width = img.shape[:2]
    
    if rotation_point is None:
        rotation_point = (width//2, height//2)
        
    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    
    return cv2.warpAffine(img, rotation_matrix, dimensions)

img_tr = translate(img, 100,250)
#cv2.imshow('transladada',img_tr)

rotacionada = rotate(img, -45)
#cv2.imshow('rotacionada',rotacionada)

#Flipping
# Flipping horizontal

flip_horizontal = cv2.flip(img, 1)
#cv2.imshow('flip horizontal',flip_horizontal)
# Flipping vertical
flip_vertical = cv2.flip(img, 0)
#cv2.imshow('flip vertical',flip_vertical)



# Flipping horizontal e vertical
flip_horizontal_e_vertical = cv2.flip(img, -1)
#cv2.imshow('flip horizontal e vertical',flip_horizontal_e_vertical)


# Resizing e cropping 

resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
#cv2.imshow('resized',resized)

cropped = img[100:300, 400:500]
cv2.imshow('crop',cropped)


cv2.waitKey(0)