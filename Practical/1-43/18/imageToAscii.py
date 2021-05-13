import sys, random, argparse
import numpy as np
import math
from PIL import Image
scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " #72 values

# A method is to sample the image down 
# to grayscale with less than 8-bit 
# precision
# Assign a character for each pixel
def ImageToAscii(fileName, factor):
    print("""
 █████╗ ███████╗ ██████╗██╗██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝██╔════╝██║██║    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████║███████╗██║     ██║██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔══██║╚════██║██║     ██║██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║  ██║███████║╚██████╗██║██║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

         -----------------------------------------------------------------------------------------------
                                    Generating File for: {}
    """.format(fileName))

    #get file and convert to gray scale (pillow)
    im = Image.open(fileName).convert('LA')
    im = im.convert ('RGB')
    width, height = im.size
    im = im.resize((math.floor(width*factor), math.floor(height*factor)), Image.ANTIALIAS)
    width, height = im.size

    #create string to store chars
    ascii = ""

    #get the lower resolution image

    #for each pixel, compute average brightness
    for x in range(width):
        for y in range(height):
            r,g,b = im.getpixel((x,y))
            brightness = (r+g+b)/3 #0 is dark (black) and 255 is bright (white)
            #find which value will represent the pixel
            location = int((brightness//3.541)-3)
            pixelChar = scale[location]
            ascii += pixelChar + " "
        ascii += '\n'
    return ascii 

def main():
    textFile = open("output.txt", "w")
    textFile.write(ImageToAscii(sys.argv[1], float(sys.argv[2])))

main()