from PIL import Image, ImageDraw, ImageFont

import math

chars = "sleepySLEEPY"[::-1]

char_array = list(chars)
charLength = len(char_array)
interval = charLength/256

scaleFactor = 0.09

char_width = 10
char_height = 18

def getChar(inputInt):
    return char_array[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")

img = Image.open("test.jpg")
img = img.convert('RGB')
fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = img.size
img = img.resize((int(scaleFactor*width), int(scaleFactor*height*(char_width/char_height))), Image.NEAREST)
width, height = img.size
pix = img.load()

outputImage = Image.new('RGB', (char_width * width, char_height * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*char_width, i*char_height), getChar(h), font = fnt, fill = (r, g, b))

    text_file.write('\n')

outputImage.save('output.png')
