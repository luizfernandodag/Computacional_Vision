import cv2
import mediapipe as mp
import numpy as np 
import time 

# tipagem ====================
confidence = float
webccam_image = np.ndarray
rgb_tuple = tuple[int, int, int]
#coords_vector

# classe =====================

class Detector:
    def __init__(self,
                 mode:bool=False,
                 number_hands:int=2,
                 model_complexity: int=1,
                 min_detect_confidence:confidence=0.5,
                 min_tracking_confidence:confidence=0.5,):
        self.mode = mode 
        self.max_num_hands = number_hands
        self.complexity = model_complexity
        self.detection_con = min_detect_confidence
        self.tracking_con = min_tracking_confidence
        
        #inicializar o hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode,
                                            self.max_num_hands,
                                            self.complexity,
                                            self.detection_con,
                                            self.tracking_con)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4,8,12,16,20]
        
    def find_hands(self,
                   img: webccam_image,
                   draw_hands:bool=True):
        #Correção de cor
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #Coletar resultados do processo das hands e analisar
        self.results = self.hands.process(img_RGB)
        
        if self.results.multi_hand_landmarks and draw_hands:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)
        
        return img
    def find_position(self,
                     img: webccam_image,
                     hand_number: int = 0):
        
        self.required_landmark_list = []
        my_hand= None
        
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_number]
            height, width,_ = img.shape
            for id, lm in enumerate(my_hand.landmark):
                center_x, center_y = int(lm.x*width), int(lm.y*width)
                self.required_landmark_list.append([id, center_x, center_y])
            
            
        
        return  self.required_landmark_list
            

# Teste de classe ==============
if __name__ == '__main__':
    
     #Coletando o framerate FPS
    previous_time = 0
    current_time = 0
     
     
     
    #Classe
    Detec = Detector()
    # Captura de imagem
    capture = cv2.VideoCapture(0)
    
    # manipulação frame
    
  
    
    while True:
       
        
        
        
        #captura de frame
        _, img = capture.read()
        
        img = Detec.find_hands(img)
        
        #Manipula de frame
        landmark_list = Detec.find_position(img)
        if landmark_list:
            print(landmark_list[8])# dedo indicador
            
        #calculando fps
        current_time = time.time()
        fps = 1/(current_time - previous_time)
        previous_time = current_time
        
        #Mostrando frame
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,255),3)
        cv2.imshow('Câmera Luiz', img)
        
        #testes
        
        #teste = Detec.find_position(img)
        #print(teste)
        
        #quit
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        
