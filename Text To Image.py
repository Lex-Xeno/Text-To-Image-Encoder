from random import randint
from PIL import Image, ImageDraw

while(1):
    TargetText = input("\nPROGRAM:\n    " + "Input a text string to be encoded.\n" + "\nUSER INPUT:\n    ")
    if len(TargetText) > 41665:
        TargetText = input("\nPROGRAM:\n    " + "\nText string too long.\nText string cannot exceed 41,665 characters." + "\nUSER INPUT:\n    ")
    else:
        break
UpperCaseColours = [(9), (18), (27), (36), (45), (54), (63), (72), (81), (90), (99), (108), (117), (126), (135), (144), (153), (162), (171), (180), (189), (198), (207), (216), (225), (234)]
UpperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
LowerCaseColours = [(9), (18), (27), (36), (45), (54), (63), (72), (81), (90), (99), (108), (117), (126), (135), (144), (153), (162), (171), (180), (189), (198), (207), (216), (225), (234)]
LowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
SymbolColours = [(6), (12), (18), (24), (30), (36), (42), (48), (54), (60), (66), (72), (78), (84), (90), (96), (102), (108), (114), (120), (126), (132), (138), (144), (150), (156), (162), (168), (174), (180), (186), (192), (198), (204), (210), (216), (222), (228), (234), (240), (246), (252)]
Symbols = ["1", "!", "2", "\"", "3", "£", "4", "$", "5", "%", "6", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", "@", "#", "~", "\\", "|", ",", "<", ".", ">", "/", "?", " "]
PixelCoordinates = []
Colours = []
PixelSpacing = []
ImageSize = 500
Count = 0
YCoordinate = 0
OutImage = Image.new("RGBA", (ImageSize, ImageSize), (0, 0, 0))
ImageDraw = ImageDraw.ImageDraw(OutImage)

for A in range(len(TargetText)):
    Rand = randint(a=1, b=5)
    PixelSpacing.append(Rand)
    if Count + Rand >= ImageSize:
        YCoordinate += 1
        Count = (Count + Rand) % ImageSize
    else:
        Count += Rand
    for B in range(len(UpperCaseLetters)):
        if TargetText[A] == UpperCaseLetters[B]:
            PixelCoordinates.append((Count, YCoordinate))
            Colours.append((UpperCaseColours[B], 0, 0))
    for B in range(len(LowerCaseLetters)):
        if TargetText[A] == LowerCaseLetters[B]:
            PixelCoordinates.append((Count, YCoordinate))
            Colours.append((0, LowerCaseColours[B], 0))
    for B in range(len(SymbolColours)):
        if TargetText[A] == Symbols[B]:
            PixelCoordinates.append((Count, YCoordinate))
            Colours.append((0, 0, SymbolColours[B]))

for X in range(ImageSize):
    for Y in range(ImageSize):
        ImageDraw.point((X, Y), (randint(a=0, b=255), randint(a=0, b=255), randint(a=0, b=255)))
for A in range(len(PixelCoordinates)):
    ImageDraw.point(PixelCoordinates[A], Colours[A])
YCoordinate = (ImageSize - 1)
Count = 0
for A in range(len(PixelSpacing)):
    if (ImageSize - 1) - Count < 0:
        YCoordinate -= 1
        Count = 0
        ImageDraw.point(((ImageSize - 1) - Count, YCoordinate), (PixelSpacing[A] * 51, randint(a=0, b=255), randint(a=0, b=255)))
    else:
        ImageDraw.point(((ImageSize - 1) - Count, YCoordinate), (PixelSpacing[A] * 51, randint(a=0, b=255), randint(a=0, b=255)))
    Count += 1

OutImage.save(input("\nPROGRAM:\n    " + "Enter save file path and name in the format:\n    Drive\Directory\Save File Name\n    E.G.\n    E:\Text To Image\EncodedImage" + "\nUSER INPUT:\n    ") + ".bmp")
print("\nPROGRAM:\n    " + "Encryption complete.\n")