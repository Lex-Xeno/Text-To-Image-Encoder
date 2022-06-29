from random import randint # Importing randint to generate the random pixel values.
from PIL import Image, ImageDraw # Importing Image to read and save the image. Importing ImageDraw to generate the outputted image.

while(1): # Starting while loop to keep the programme going if there is an error in the inputted text.
    TargetText = input("\nPROGRAMME:\n    Input a text string to be encoded.\nUSER:\n    ") # Asking for an input from the user.
    if len(TargetText) > 41665: # Checking if the user exceeded the character limit.
        TargetText = input("\nPROGRAMME:\n    Text string too long.\nText string cannot exceed 41,665 characters.\nUSER:\n    ") # Informing the user that they have exceeded the character limit.
    else: # If the user hasn't exceeded the character limit.
        break # Breaking out of the while loop

UpperCaseColours = [(9), (18), (27), (36), (45), (54), (63), (72), (81), (90), (99), (108), (117), (126), (135), (144), (153), (162), (171), (180), (189), (198), (207), (216), (225), (234)] # Creating a list of colour values for the red RGB band. This list corresponds to the UpperCaseLetters list.
UpperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # Creating a list of uppercase letters for the programme to check through. This list is used to get the correct index for the UpperCaseColours list.

LowerCaseColours = [(9), (18), (27), (36), (45), (54), (63), (72), (81), (90), (99), (108), (117), (126), (135), (144), (153), (162), (171), (180), (189), (198), (207), (216), (225), (234)] # Creating a list of colour values for the green RGB band. This list corresponds to the LowerCaseLetters list.
LowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Creating a list of lowercase letters for the programme to check through. This list is used to get the correct index for the LowerCaseColours list.

SymbolColours = [(6), (12), (18), (24), (30), (36), (42), (48), (54), (60), (66), (72), (78), (84), (90), (96), (102), (108), (114), (120), (126), (132), (138), (144), (150), (156), (162), (168), (174), (180), (186), (192), (198), (204), (210), (216), (222), (228), (234), (240), (246), (252)] # Creating a list of colour values for the blue RGB band. This list corresponds to the Symbols list.
Symbols = ["1", "!", "2", "\"", "3", "£", "4", "$", "5", "%", "6", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", "@", "#", "~", "\\", "|", ",", "<", ".", ">", "/", "?", " "] # Creating a list of symbols for the programme to check through. This list is used to get the correct index for the SymbolColours list.

PixelCoordinates = [] # Creating an empty list to hold the coordinates for the pixels that hold the input text characters.
Colours = [] # Creating an empty list to hold the colours for the input text characters.
PixelSpacing = [] # Creating an empty list to hold the spacing between the pixels so that the decoder knows what pixels hold the input text characters.
ImageSize = 500 # Setting the base image size.
Count = 0 # Creating a variable to be used to keep count of different indexes.
YCoordinate = 0 # Creating a variable to keep count of the Y axis.
OutImage = Image.new("RGB", (ImageSize, ImageSize), (0, 0, 0)) # Creating the image to put the encoded imformation on.
ImageDraw = ImageDraw.ImageDraw(OutImage) # Assigning the ImageDraw function to a shorter version to make coding easier.

for A in range(len(TargetText)): # Starting the loop to assign the coordinates, colours and spacing to the pixels that hold the inputted text.
    Rand = randint(a=1, b=5) # Generating a random integer and holding it to assign it to other variables.
    PixelSpacing.append(Rand) # Appending the previously generated random integer to PixelSpacing.
    if Count + Rand >= ImageSize: # Checking if the coordinate is going to be on the image.
        YCoordinate += 1 # Moving up the Y axis to continue generating coordinates.
        Count = (Count + Rand) % ImageSize # Adding on the excess distance to the next line up the Y axis.

    else: # Continuing if the coordinate is on the image.
        Count += Rand # Adding Rand to Count to get the next coordinate.

    for B in range(len(UpperCaseLetters)): # Cycling through the uppercase letters in the list UpperCaseLetters.
        if TargetText[A] == UpperCaseLetters[B]: # Checking for what uppercase letter is in the inputted text string's A index.
            PixelCoordinates.append((Count, YCoordinate)) # Appending the coordinate to the PixelCoordinates list.
            Colours.append((UpperCaseColours[B], 0, 0)) # Appending the correct colour to the Colour list.

    for B in range(len(LowerCaseLetters)): # Cycling through the lowercase letters in the list LowerCaseLetters.
        if TargetText[A] == LowerCaseLetters[B]: # Checking for what lowercase letter is in the inputted text string's A index.
            PixelCoordinates.append((Count, YCoordinate)) # Appending the coordinate to the PixelCoordinates list.
            Colours.append((0, LowerCaseColours[B], 0)) # Appending the correct colour to the Colour list.

    for B in range(len(SymbolColours)): # Cycling through the symbols in the list Symbols.
        if TargetText[A] == Symbols[B]: # Checking for what symbol is in the inputted text string's A index.
            PixelCoordinates.append((Count, YCoordinate)) # Appending the coordinate to the PixelCoordinates list.
            Colours.append((0, 0, SymbolColours[B])) # Appending the correct colour to the Colour list.

for X in range(ImageSize): # Starting the loop to keep track of the X axis.
    for Y in range(ImageSize): # Starting the loop to keep track of the Y axis.
        ImageDraw.point((X, Y), (randint(a=1, b=255), randint(a=1, b=255), randint(a=1, b=255))) # Plotting the pixels that fill in the gaps of the image.

for A in range(len(PixelCoordinates)): # Starting the loop that plots the pixels that contain the inputed text string's characters.
    ImageDraw.point(PixelCoordinates[A], Colours[A]) # plotting the pixels that contain the inputted text string's characters.

YCoordinate = (ImageSize - 1) # Resetting YCoordinate with an offset to keep the values within the range of the image.
Count = 0 # Resetting Count.

for A in range(len(PixelSpacing)): # Starting the loop that plots the points for the pixel spacing for the decoder to decode the image.
    if (ImageSize - 1) - Count < 0: # Checking that the coordinate is still on the image.
        YCoordinate -= 1 # Moving down the Y axis.
        Count = 0 # Resetting Count.
    ImageDraw.point(((ImageSize - 1) - Count, YCoordinate), (PixelSpacing[A] * 51, 0, randint(a=0, b=255))) # Plotting the point for the decoder to use to decode the image.
    Count += 1 # Increasing Count by 1 to move to the next coordinate.

print("\nPROGRAMME:\n    Encryption complete.") # Confirming that the encryption has completed.
OutImage.save(input("\nPROGRAMME:\n    Enter save file path and name (without the file extension) in the format:\n    Drive\Directory\Save File Name\n\n    E.G.\n    E:\Text To Image Encoder\EncodedImage\nUSER:\n    ") + ".bmp") # Asking where to save the image and it's file name.
print("\nPROGRAMME:\n    Image saved successfully.") # Confirming that the image was saved.