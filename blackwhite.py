from PIL import Image
#pip install Pillow
img= Image.open("images.jpg")
blackAndWhite = img.convert("L")
blackAndWhite.save('bw_images.jpg')
blackAndWhite.show()
