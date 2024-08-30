import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

age_net = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/age_deploy.prototxt', 'D:/Pranav/class python/Techraiance 24/age_net.caffemodel')
gender_net = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/gender_deploy.prototxt', 'D:/Pranav/class python/Techraiance 24/gender_net.caffemodel')

age_brackets = ['(0-5)', '(5-10)', '(10-15)','(15-20)', '(20-25)', '(25-35)', '(35-45)', '(45-60)','(60-100)']

face_cascade = cv2.CascadeClassifier("D:/Pranav/class python/Techraiance 24/haarcascade_frontalface_default.xml")

emotion_classifier = load_model("D:/Pranav/class python/Techraiance 24/model.h5")
emotions = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture (0)
while 1 :
    ret, frame = cap.read()
    
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    trained = face_cascade.detectMultiScale(grey)

    blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

    age_net.setInput(blob)
    age_preds = age_net.forward()
    age_bracket_index = age_preds[0].argmax()
    age_bracket = age_brackets [age_bracket_index]

    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = "Male" if gender_preds[0][0] > 0.5 else "Female"
    
    
    
    for x,y,w,h in trained:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_grey = grey[y:y+h,x:x+w]
        roi_grey = cv2.resize(roi_grey,(48,48),interpolation=cv2.INTER_AREA)
        if np.sum([roi_grey])!= 0 :
            roi = roi_grey.astype("float")/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)
            emotion_preds = emotion_classifier.predict(roi)[0]
            emotion = emotions[emotion_preds.argmax()]
        cv2.putText(frame, f"Gender:{gender}",(x+w+10,y),cv2.FONT_HERSHEY_PLAIN,1.3,(168,151,106),2)
        cv2.putText(frame, f"Age:{age_bracket}",(x+w+10,y+30),cv2.FONT_HERSHEY_PLAIN,1.3,(168,151,106),2)
        cv2.putText(frame, f"Emotion:{emotion}",(x+w+10,y+60),cv2.FONT_HERSHEY_PLAIN,1.3,(168,151,106),2)

    cv2.imshow("Gender and Age and Emotion Prediction",frame)
    k = cv2.waitKey(1)& 0xFF
        
    if k==81 or k == 113:
        break

cap.release()
cv2.destroyAllWindows()