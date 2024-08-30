import cv2
import matplotlib.pyplot as plt

age_net = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/age_deploy.prototxt', 'D:/Pranav/class python/Techraiance 24/age_net.caffemodel')
gender_net = cv2.dnn.readNetFromCaffe('D:/Pranav/class python/Techraiance 24/gender_deploy.prototxt', 'D:/Pranav/class python/Techraiance 24/gender_net.caffemodel')

age_brackets = ['(0-5)', '(5-10)', '(10-15)','(15-20)', '(20-25)', '(25-35)', '(35-45)', '(45-60)','(60-100)']

Image = cv2.imread("D:/Pranav/class python/Techraiance 24/5monkeys.png")

blob = cv2.dnn.blobFromImage(Image, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

age_net.setInput(blob)
age_preds = age_net.forward()
age_bracket_index = age_preds[0].argmax()
age_bracket = age_brackets [age_bracket_index]

gender_net.setInput(blob)
gender_preds = gender_net.forward()
gender = "Male" if gender_preds[0][0] > 0.5 else "Female"

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(Image,cv2.COLOR_BGR2RGB))
plt.title(f'Gender: {gender}, ' + f'Age: {age_bracket}')
plt.axis("off")
plt.show()