import sys, random, argparse
import numpy as np
import math
from PIL import Image
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# A method is to sample the image down 
# to grayscale with less than 8-bit 
# precision
# Assign a character for each pixel
def ImageToAscii(fileName):
    print("Generating image for file: " + fileName) 
    #get file and convert to gray scale (pillow)
    im = Image.open(fileName).convert('LA')
    return assignCharater(im)

def assignCharater(im):
    width, height = im.size

def main():
    print(ImageToAscii(sys.argv[1]))

main()