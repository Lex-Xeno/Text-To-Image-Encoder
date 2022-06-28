from PIL import Image

print("\nPROGRAM:\n    " + "Enter encrypted image filepath.")
TargetImage = Image.open(input("\nUSER INPUT:\n    "))
UpperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
UpperCaseNumbers = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234]
LowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
LowerCase = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234]
Symbols = ["1", "!", "2", "\"", "3", "£", "4", "$", "5", "%", "6", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", "@", "#", "~", "\\", "|", ",", "<", ".", ">", "/", "?", " "]
SymbolColours = [(6), (12), (18), (24), (30), (36), (42), (48), (54), (60), (66), (72), (78), (84), (90), (96), (102), (108), (114), (120), (126), (132), (138), (144), (150), (156), (162), (168), (174), (180), (186), (192), (198), (204), (210), (216), (222), (228), (234), (240), (246), (252)]
PixelSpacing = []
ImageSize = 500
Count = 0
OutText = ""

print("\nPROGRAM:\n    " + "Decripting...\n    This may take a while...")
while(1):
    if TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 51:
        PixelSpacing.append(1)
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 102:
        PixelSpacing.append(2)
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 153:
        PixelSpacing.append(3)
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 204:
        PixelSpacing.append(4)
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 255:
        PixelSpacing.append(5)
    else:
        break
    Count += 1

Count = 0

for A in range(len(PixelSpacing)):
    Count += PixelSpacing[A]
    for B in range(len(UpperCaseNumbers)):
        if TargetImage.getdata(band=0)[Count] == UpperCaseNumbers[B] and TargetImage.getdata(band=1)[Count] == 0 and TargetImage.getdata(band=2)[Count] == 0:
            OutText += UpperCaseLetters[B]
    for B in range(len(LowerCase)):
        if TargetImage.getdata(band=0)[Count] == 0 and TargetImage.getdata(band=1)[Count] == LowerCase[B] and TargetImage.getdata(band=2)[Count] == 0:
            OutText += LowerCaseLetters[B]
    for B in range(len(Symbols)):
        if TargetImage.getdata(band=0)[Count] == 0 and TargetImage.getdata(band=1)[Count] == 0 and TargetImage.getdata(band=2)[Count] == SymbolColours[B]:
            OutText += Symbols[B]

print("\nPROGRAM:\n    " + "Decripted text reads:\n    " + OutText)