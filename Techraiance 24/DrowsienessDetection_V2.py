import cv2
import mediapipe as mp
from scipy.spatial import distance

mp_face_mesh = mp.solutions.face_mesh
mp_face_draw = mp.solutions.drawing_utils

face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    
    success,frame = cap.read()
    
    threshold = 0.28
    
    frames = 0
    drowsie_frames = 0
    
    
    def eyesAspectRatio(eyes) :
        A = distance.euclidean(eyes[1],eyes[5])
        B = distance.euclidean(eyes[2],eyes[4])
        C = distance.euclidean(eyes[0],eyes[3])       
        return (A+B)/(2.0*C)
    
    results = face_mesh.process(frame)
    if results.multi_face_landmarks :
        for face_landmark in results.multi_face_landmarks:
            Left_Eye = [(point.x,point.y)for point in face_landmark.landmark[159:145:-1]]
            
            Right_Eye = [(point.x,point.y)for point in face_landmark.landmark[386:380:-1]]
            
            left_EAR = eyesAspectRatio(Left_Eye)
            right_EAR = eyesAspectRatio(Right_Eye)
            
            average_EAR = (left_EAR + right_EAR)/2.0
            
            # mp_face_draw.draw_landmarks(frame,face_landmark)
            
            if average_EAR > threshold:
                frames += 1
                print('awake')
                drowsie_frames = 0
            elif average_EAR < threshold:
                drowsie_frames += 1
                print('drowsy')
                frames = 0
            
    cv2.imshow("test",frame)
    
    
    k = cv2.waitKey(1)& 0xFF
        
    if k==81 or k == 113:
        break

cap.release()
cv2.destroyAllWindows()