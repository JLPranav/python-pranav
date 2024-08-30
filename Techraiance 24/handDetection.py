import cv2
import mediapipe as mp
import imutils

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode = False,max_num_hands = 2,min_detection_confidence = 0.5,min_tracking_confidence = 0.5)

cap = cv2.VideoCapture(0)

while True:
    success,frame = cap.read()
    
    #post processing
    frame = imutils.resize(frame,500)
    
    result = hands.process(frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)
        
    cv2.flip(frame,0)
            
    cv2.imshow("Hand Detection",frame)
    
    k = cv2.waitKey(1)& 0xFF
    
    if k==81 or k == 113:
        break
    
cap.release()