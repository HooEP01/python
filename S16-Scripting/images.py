from PIL import Image, ImageFilter

image = Image.open('./Pokedex/pikachu.jpg')
filtered_img = image.filter(ImageFilter.BLUR)
# filtered_img = image.filter(ImageFilter.SHARPEN)
filtered_img = image.convert('L')
filtered_img.save('blur.png', 'png')
# jpg
print(image.format)

# (640, 640)
print(image.size)

# RGB
print(image.mode)

# print(dir(image))
