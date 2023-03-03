from PIL import Image

im = Image.open(r"lab7pic.jpg")

width, height = im.size

left = 4
top = height / 5
right = 154
bottom = 3 * height / 5

im1 = im.crop((left, top, right, bottom))
newsize = (300, 300)
im1 = im1.resize(newsize)

im1.show()