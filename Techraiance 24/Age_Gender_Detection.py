# import cv2
# import imutils

# age_prediction = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/age_deploy.prototxt','D:/Pranav/class python/Techraiance 24/age_net.caffemodel')
# gender_prediction = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/gender_deploy.prototxt','D:/Pranav/class python/Techraiance 24/gender_net.caffemodel')

# age_brackets = ["(0-3)","(4-7)","(8-13)","(14-20)","(21-32)","(33-43)","(44-53)","(54-100)"]

# cap = cv2.VideoCapture(0)
# success,frame = cap.read()
# img = imutils.resize(frame,width=1000)

# blob = cv2.dnn.blobFromImage(frame,1.0,(277,277),(147,46,0),swapRB=False)

# age_prediction.setInput(blob)
# age_preds = age_prediction.forward()

# gender_prediction.setInput(blob)
# gender_preds = gender_prediction.forward()

# age_bracket_index = age_preds[0].argmax()
# age_bracket = age_brackets[age_bracket_index]

# gender = 'Male' if gender_preds[0][0]>0.5 else "Female"

# print("Predicted Age Bracket {}".format(age_bracket))
# print("Predicted Gender {}".format(gender))

# cv2.imshow("AGE & GENDER Predition",frame)
# cv2.waitkey(0)
# cap.release()
# cv2.destroyAllWindows()

import cv2
import imutils

age_net = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/age_deploy.prototxt', 'D:/Pranav/class python/Techraiance 24/age_net.caffemodel')
gender_net = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/gender_deploy.prototxt', 'D:/Pranav/class python/Techraiance 24/gender_net.caffemodel')

age_brackets = ['(0-2)', '(4-8)', '(9-15)','(16-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

cap = cv2.VideoCapture (0)
ret, frame = cap.read()
img_r = imutils.resize(frame, width=1000)

blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

age_net.setInput(blob)
age_preds = age_net.forward()
age_bracket_index = age_preds[0].argmax()
age_bracket = age_brackets [age_bracket_index]

gender_net.setInput(blob)
gender_preds = gender_net.forward()
gender = "Male" if gender_preds[0][0] > 0.5 else "Female"

print("Predicted Age Bracket: {}".format(age_bracket))
print("Predicted Gender: {}".format(gender))

cv2.imshow("Gender and Age Prection",frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()