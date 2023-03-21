from PIL import Image
from PIL import ImageFilter

from PIL.ImageFilter import (  BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

img = Image.open(r"lab7pic.jpg")

img1 = img.filter(CONTOUR)
img1.show()
