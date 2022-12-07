from PIL import Image, ImageFilter

SOURCE_DIR = 'images/'

first = Image.open(SOURCE_DIR + '1.jpg')
second = Image.open(SOURCE_DIR + '2.jpg')
second = second.resize((300, 300))

r, g, b = second.split()
img1 = Image.merge('RGB', (r, g, b))
img2 = Image.merge('RGB', (r, g.filter(ImageFilter.GaussianBlur(25)), b))
second.show()
first.show()
img1.show()
img2.show()
