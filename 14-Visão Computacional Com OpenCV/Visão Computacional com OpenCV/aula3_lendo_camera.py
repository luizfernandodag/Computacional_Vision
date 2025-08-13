import cv2
import numpy as np

# web cams pessoais 0,1,... 
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("Gravação Fernando",frame)
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
    
cap.release()
cv2.destroyAllWindows()