import sys, random, argparse
import numpy as np
import math
  
from PIL import Image
  
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def getAverageL(image):
  
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)
  
    # get shape
    w,h = im.shape
  
    # get average
    return np.average(im.reshape(w*h))
  
def covertImageToAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images 
    """
    # declare globals
    global gscale1, gscale2
  
    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')
  
    # store dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))
  
    # compute width of tile
    w = W/cols
  
    # compute tile height based on aspect ratio and scale
    h = w/scale
  
    # compute number of rows
    rows = int(H/h)
      
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
  
    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
  
    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
  
        # correct last tile
        if j == rows-1:
            y2 = H
  
        # append an empty string
        aimg.append("")
  
        for i in range(cols):
  
            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
  
            # correct last tile
            if i == cols-1:
                x2 = W
  
            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))
  
            # get average luminance
            avg = int(getAverageL(img))
  
            gsval = gscale1[int((avg*69)/255)]
  
            # append ascii char to string
            aimg[j] += gsval
      
    # return txt image
    return aimg
  
# main() function
def main():
    # create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
  
    # parse args
    args = parser.parse_args()
    
    imgFile = args.imgFile
  
    # set output file
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
  
    # set scale default as 0.43 which suits
    # a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
  
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)
  
    print('generating ASCII art...')
    # convert image to ascii txt
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)
  
    # open file
    f = open(outFile, 'w')
  
    # write to file
    for row in aimg:
        f.write(row + '\n')
  
    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)
  
if __name__ == '__main__':
    main()


# import sys, random, argparse
# import numpy as np
# import math
  
# from PIL import Image
# #set gray scale of 70
# grayScale = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". """
# argImage = sys.argv[1]

# def getAverageGrayScale(image):
#     array = np.array(image)
#     w = array.shape[0]
#     h = array.shape[1]
#     return np.average(array.flatten())

# def imageToAscii(imageName, cols):
#     #loading image to PIL format
#     image = Image.open(imageName).convert('LA')
#     #creating vars from image
#     W, H = image.size
#     #using scale that suite most fonts
#     scale = 0.43
#     w = W/cols
#     h = w/scale
#     rows = int(H/h)
#     #creating a empty char array
#     imageArray = []


#     for i in range(rows):
#         y1 = int(i*h)
#         y2 = int((i+1)*h)
#         if i == rows-1:
#             y2 = h
#         imageArray.append("")
#         for j in range(cols):
#             x1 = int(j*w)
#             x2 = int((j+w)*w)
#             if j == cols-1:
#                 x2 = W
#             img = image.crop((x1, y1, x2, y2))
#             avg = int(getAverageGrayScale(image))
#             grayScaleValue = grayScale[int((avg*69)/255)]
#             imageArray[i] += grayScaleValue
#     print(arrayImage)
#     return imageArray

# #printing the image:
# #get the file
# string = imageToAscii("test2.jpg", 80)
# print(string)

