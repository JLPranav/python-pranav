import cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/Pranav/class python/Techraiance 24/download.jpeg")
image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image2 = cv2.medianBlur(image2,1)

print(image.shape)

cv2.imshow("Porshe 911",image)
cv2.imshow("Porshe_911",image1)
cv2.imshow("Porshe_911 Gray",image2)

cv2.waitKey(0)

cv2.destroyAllWindows()