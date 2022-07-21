from PIL import Image
image = Image.open("c.jpeg")
print(image)
info = image._getexif()
image.show()
print image.getpixel(10,10)
print image.getpixel(10,10)
print info
print "kamera marka:",info[271]
print "kamera model:",info[272]
print "tarih:",info[36867]
