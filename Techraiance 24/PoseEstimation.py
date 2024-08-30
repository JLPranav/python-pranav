import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

while True:
    success,frame  = cap.read()
    
    pose = mp_pose.Pose(min_detection_confidence = 0.5,min_tracking_confidence = 0.5)
    results = pose.process(frame)
    try:
        landmarks = results.pose_landmarks.landmark
    except:
        pass
    
    mp_drawing.draw_landmarks(frame,results.pose_landmarks,
                              mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color = (255,0,0),thickness = 2,circle_radius = 2),
                              mp_drawing.DrawingSpec(color = (0,255,0),thickness = 2))
    
    
    
    
    cv2.imshow("Pose Estimation",frame)
    k = cv2.waitKey(1)& 0xFF
        
    if k==81 or k == 113:
        break

cap.release()
cv2.destroyAllWindows()