import cv2

cap = cv2.VideoCapture("OpenCV/assets/videos/dog.mp4")

while True:
    _, frame = cap.read()
    
    cv2.imshow('video do dog', frame)
    #cv2.waitKey(20) pode teronar mais que #FF
    #mascara cv2.waitKey(20)& 0xFF
    
    if cv2.waitKey(20)& 0xFF==ord('d'): # -215 assertion failed
        break
    
cap.release()
cv2.destroyAllWindows()