from PIL import Image

#read the image
im = Image.open("city.jpg")

#image size
# 4435, 2952
size=(4435, 2952)
#resize image
out = im.resize(size)
#save resized image
out.save('bigcity.jpg')