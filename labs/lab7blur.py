from PIL import Image
from PIL import ImageFilter

im = Image.open(r"lab7pic.jpg")

im1 = im.filter(ImageFilter.BoxBlur(4))

im1.show()