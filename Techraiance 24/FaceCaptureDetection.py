import cv2
import random

face_cascade = cv2.CascadeClassifier("D:/Pranav/class python/Techraiance 24/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("D:/Pranav/class python/Techraiance 24/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("D:/Pranav/class python/Techraiance 24/haarcascade_smile.xml")

capture = cv2.VideoCapture(0)


while 1:
    success,image = capture.read()
    

    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    trained = face_cascade.detectMultiScale(grey)

    # print(trained)

    # x,y,w,h = trained[0]

    for x,y,w,h in trained:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        eye_grey = grey[y:y+h,x:x+w]
        eye_img = image[y:y+h,x:x+w]
        trained_eye = eye_cascade.detectMultiScale(eye_grey)
        for ex,ey,ew,eh in trained_eye:
            cv2.rectangle(eye_img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        trained_smile = smile_cascade.detectMultiScale(eye_grey,2.8,5)
        for sx,sy,sw,sh in trained_smile:
            cv2.rectangle(eye_img,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

    cv2.imshow("image",image)

    k = cv2.waitKey(1)& 0xFF
    
    if k==81 or k == 113:
        break

capture.release()
    
    