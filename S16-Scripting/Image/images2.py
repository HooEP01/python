from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filter_img = img.convert('L')
crooked = filter_img.rotate(90)
resize = crooked.resize((300, 300))
box = (100, 100, 400, 400)
region = filter_img.crop(box)
region.save('grey.png', 'png')
region.show()
