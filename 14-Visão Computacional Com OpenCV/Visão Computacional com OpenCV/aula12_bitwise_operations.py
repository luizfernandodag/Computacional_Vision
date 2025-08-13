import cv2 
import numpy as np

blank = np.zeros([400,400], dtype='uint8')
cv2.imshow('blank', blank)

rectangle = cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1 )
circle = cv2.circle(blank.copy(),(200,200), 200, 255,-1)

#cv2.imshow('Ret', rectangle)
cv2.imshow('Cir', circle)

#AND ambos são 1 (branco)
bitwise_and = cv2.bitwise_and(rectangle,circle)
#cv2.imshow('and',bitwise_and)

#OR qualquer um branco

bitwise_or = cv2.bitwise_or(rectangle, circle)
#cv2.imshow('or',bitwise_or)

# XOR (um ou outro)

bitwise_xor = cv2.bitwise_xor(rectangle, circle)
#cv2.imshow('xor', bitwise_xor)

# NOT

bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('circle NOT', bitwise_not)


cv2.waitKey(0)