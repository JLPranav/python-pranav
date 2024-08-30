import cv2
import tkinter.filedialog as fd

path = fd.askopenfilename()

image = cv2.imread(path)
image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# image2 = cv2.medianBlur(image2,1)
edges = cv2.adaptiveThreshold(image2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,7)
filter = cv2.bilateralFilter(image2,9,300,300)
cartooning = cv2.bitwise_and(filter,filter,mask=edges)

print(image.shape)

# cv2.imshow("Porshe 911",image)
# cv2.imshow("Porshe_911",image1)
# cv2.imshow("Porshe_911 Gray",image2)
cv2.imshow("Porshe 911 Cartoony",cartooning)

cv2.waitKey(0)

cv2.destroyAllWindows()