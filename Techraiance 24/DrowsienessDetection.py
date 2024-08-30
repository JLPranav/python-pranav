import cv2

eye_cascade = cv2.CascadeClassifier("D:/Pranav/class python/Techraiance 24/haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier("D:/Pranav/class python/Techraiance 24/haarcascade_frontalface_default.xml")

VidCap = cv2.VideoCapture(0)

#TRESHNOLDS#
drowsiness = 2
awake = 1
#//////////#

#FRAMES#
drowsieness_frames = 0
awake_frames = 0
#//////#

while True:
    success,frame = VidCap.read()
    
    if not success:
        break
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    trained_face = face_cascade.detectMultiScale(grey)
    for x,y,w,h in trained_face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        crop = grey[y:y+h,x:x+w]
        eye_trained = eye_cascade.detectMultiScale(crop)
        if len(eye_trained) == 0:
            drowsieness_frames += 1
            awake_frames = 0
            cv2.putText(frame, "Drowsieness",(x,y-20),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(168,151,106),5)
        else:
            drowsieness_frames = 0
            awake_frames += 1
            cv2.putText(frame, "Awakeness",(x,y-20),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(168,151,106),5)
        
        
    cv2.imshow("Drowsieness detection",frame)
    if drowsieness_frames > drowsiness :
        print("Drowsy")
    if awake_frames > awake:
        print("awake")
    
    k = cv2.waitKey(1)& 0xFF
    
    if k==81 or k == 113:
        break

cv2.destroyAllWindows()
VidCap.release()