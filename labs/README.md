# Lab 7

Here is how you can run a the python scripts with pillow on creating a blurred or filtered image and resizing it.

First in your windows command prompt, run:

**pip install pillow**

Now that pillow is installed, lets open up code writer to begin the script.

Before we start coding make sure you have Downloaded an image from the internet and save it to your hard drive.

For our first script we will blur an Image.

In code write under the python file you have created run:

**from PIL import Image**

**from PIL import ImageFilter**

#open your chosen image by placing the name in place of "lab7pic.jpg"

**im = Image.open(r"lab7pic.jpg")**


#below function Blurs the image by setting each pixel to the average value of the pixels
#in a square box extending radius pixels in each direction.

**im1 = im.filter(ImageFilter.BoxBlur(4))** 

#opens your image to show what was changed in photos app

**im1.show()**


# Part 2: Filtering

For our Second script we will blur an Image.

In code writer under the python file you have created run:

**from PIL import Image**

**from PIL import ImageFilter**

#the following functions will create a sharpened filtered effect 

**from PIL.ImageFilter import (  BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)**

**img = Image.open(r"lab7pic.jpg")**

#the following function will create a grayscale filtered effect  

**img1 = img.filter(CONTOUR)**

**img1.show()**


# Part 3: Resizing

For our third script we will blur an Image.

In code writer under the python file you have created run:


**from PIL import Image**

**im = Image.open(r"lab7pic.jpg")**

**width, height = im.size**


#the following functions will set cropped image points

**left = 4
top = height / 5
right = 154
bottom = 3 * height / 5**

**im1 = im.crop((left, top, right, bottom))**

**newsize = (300, 300)**

**im1 = im1.resize(newsize)**

**im1.show()**
