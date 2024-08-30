from pywhatkit import image_to_ascii_art as tk
import time
x = 1
frames = input("frames: ")

for i in range(int(frames)):
    img = str(x)+".jpg"
    text_image = "text_image"
    tk(img,text_image)
    p = open(r"text_image.txt","r")
    print(p.read())
    p.close()
    time.sleep(0.01)
    x+=1