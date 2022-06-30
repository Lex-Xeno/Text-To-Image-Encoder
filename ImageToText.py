from PIL import Image # Importing Image to read and save the image.

TargetImage = Image.open(input("\nPROGRAMME:\n    Enter encrypted image file path (including the file extension).\nUSER:\n    ")) # Asking where the image you want to decrypt is.
UpperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # Creating a list of uppercase letters. This list corresponds to the UpperCaseColours list.
UpperCaseNumbers = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234] # Creating a list of colour values for the red RGB band for the program to check through. This list is used to get the correct index for the UpperCaseLetters list.
LowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Creating a list of lowercase letters. This list corresponds to the LowerCaseColours list.
LowerCase = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234] # Creating a list of colour values for the green RGB band for the program to check through. This list is used to get the correct index for the LowerCaseLetters list.
Symbols = ["1", "!", "2", "\"", "3", "£", "4", "$", "5", "%", "6", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", "@", "#", "~", "\\", "|", ",", "<", ".", ">", "/", "?", " "] # Creating a list of symbols. This list corresponds to the SymbolColours list.
SymbolColours = [(6), (12), (18), (24), (30), (36), (42), (48), (54), (60), (66), (72), (78), (84), (90), (96), (102), (108), (114), (120), (126), (132), (138), (144), (150), (156), (162), (168), (174), (180), (186), (192), (198), (204), (210), (216), (222), (228), (234), (240), (246), (252)] # Creating a list of colour values for the blue RGB band for the program to check through. This list is used to get the correct index for the Symbols list.
PixelSpacing = [] # Creating an empty list to hold the spacing between the pixels that hold the encrypted text string.
ImageSize = 500 # Setting the base image size.
Count = 0 # Creating a variable to be used to keep count of different indexes.
OutText = "" # Creating an empty string to hold the decrypted text.

print("\nPROGRAMME:\n    Decrypting...\n    This may take a while...") # Informing the user that the decrypting process is in motion.

while(1): # Starting the loop that finds the spacing between the pixels that hold the encrypted text string.
    if TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 51 and TargetImage.getdata(band=1)[((ImageSize ** 2) - 1) - Count] == 0: # Checking if the pixel corresponds to the value 1.
        PixelSpacing.append(1) # Appending the value 1.
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 102 and TargetImage.getdata(band=1)[((ImageSize ** 2) - 1) - Count] == 0: # Checking if the pixel corresponds to the value 2.
        PixelSpacing.append(2) # Appending the value 2.
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 153 and TargetImage.getdata(band=1)[((ImageSize ** 2) - 1) - Count] == 0: # Checking if the pixel corresponds to the value 3.
        PixelSpacing.append(3) # Appending the value 3.
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 204 and TargetImage.getdata(band=1)[((ImageSize ** 2) - 1) - Count] == 0: # Checking if the pixel corresponds to the value 4.
        PixelSpacing.append(4) # Appending the value 4.
    elif TargetImage.getdata(band=0)[((ImageSize ** 2) - 1) - Count] == 255 and TargetImage.getdata(band=1)[((ImageSize ** 2) - 1) - Count] == 0: # Checking if the pixel corresponds to the value 5.
        PixelSpacing.append(5) # Appending the value 5.
    else: # If there isn't a pixel that corresponds to the values 1, 2, 3, 4, or 5.
        break # The program breaks out of the while loop.
    Count += 1 # Increasing Count up by one to move to the next index.

Count = 0 # Resetting Count.

for A in range(len(PixelSpacing)): # Starting the loop that checks what each pixel corresponds to.
    Count += PixelSpacing[A] # Increasing count by PixelSpacing to get to the next coordinate.
    for B in range(len(UpperCaseNumbers)): # Checking is the pixel corresponds to an lowercase letter.
        if TargetImage.getdata(band=0)[Count] == UpperCaseNumbers[B] and TargetImage.getdata(band=1)[Count] == 0 and TargetImage.getdata(band=2)[Count] == 0: # Checking what uppercase letter that pixel corresponds to.
            OutText += UpperCaseLetters[B] # Adding the uppercase letter to the decrypted text.
    for B in range(len(LowerCase)): # Checking is the pixel corresponds to an uppercase letter.
        if TargetImage.getdata(band=0)[Count] == 0 and TargetImage.getdata(band=1)[Count] == LowerCase[B] and TargetImage.getdata(band=2)[Count] == 0: # Checking what lowercase letter that pixel corresponds to.
            OutText += LowerCaseLetters[B] # Adding the lowercase letter to the decrypted text.
    for B in range(len(Symbols)): # Checking is the pixel corresponds to an symbol.
        if TargetImage.getdata(band=0)[Count] == 0 and TargetImage.getdata(band=1)[Count] == 0 and TargetImage.getdata(band=2)[Count] == SymbolColours[B]: # Checking what symbol that pixel corresponds to.
            OutText += Symbols[B] # Adding the symbol to the decrypted text.

print("\nPROGRAMME:\n    Decrypted text reads:\n    " + OutText) # Informing the user what the decrypted text reads.