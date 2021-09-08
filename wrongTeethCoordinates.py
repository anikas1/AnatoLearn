"""
Authors: Anika Suman & Ayush Khanna
Date: 9/7/21
Class: Math 241 Scientific Computing
Professor: Ben Marlin
"""

from PIL import Image
import random

img = Image.open("images\wrongteethcoor.png") #load the image
size = w,h = img.size
data = img.load()

#any color other than black is appended to a coordinate containing the wrong coordinates
pieces = []
#for every pixel
for x in range(w):
    for y in range(h):
        hex_color = '#' + ''.join([ hex(it)[2:].zfill(2).upper() for it in data[x,y]]) #scan in the color of each pixel
        if not (hex_color.startswith('#000000')): #if pixel is not black
            pieces.append((x,y)) #add the (x,y) position to the array