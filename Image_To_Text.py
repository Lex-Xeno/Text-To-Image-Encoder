from PIL import Image

TargetImage = Image.open(input("\nPROGRAMME:\n    Enter encrypted image file path (including the file extension).\nUSER:\n    ")) # Asking where the image you want to decrypt is.
Count = 0 # Creating a variable to be used to keep count of different indexes.
LetterColours = [] # Creating an empty list to hold the colour values for the red (if the specified letter is an uppercase letter) and green (if the specified letter is a lowercase letter) RGB band. This list corresponds to the Letters list.
SymbolColours = [] # Creating an empty list to hold the colour values for the blue RGB band. This list corresponds to the Symbols list.
Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # Creating a list of lowercase letters for the programme to check through. This list is used to get the correct index for the LowerCaseColours list.
Symbols = ["1", "!", "2", "\"", "3", "£", "4", "$", "5", "%", "6", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", "@", "#", "~", "\\", "|", ",", "<", ".", ">", "/", "?", " "] # Creating a list of symbols for the programme to check through. This list is used to get the correct index for the SymbolColours list.

for A in range(len(Letters)): # Starting the loop that calculates and appends the colour values for LetterColours.
    Count += 1 # Increasing Count by 1 to move to the next index.
    LetterColours.append(round((255 / len(Letters)) * Count)) # Apending the colour value to LetterColours.

Count = 0 # Reseting Count.

for A in range(len(Symbols)): # Starting the loop that calculates and appends the colour values for SymbolColours.
    Count += 1 # Increasing Count by 1 to move to the next index.
    SymbolColours.append(round((255 / len(Symbols)) * Count)) # Apending the colour value to SymbolColours.
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
    if TargetImage.getdata(band=0)[Count] == 0 and TargetImage.getdata(band=1)[Count] > 0 and TargetImage.getdata(band=2)[Count] == 0: # Checking if the pixel corresponds to a lowercase letter.
        for B in range(len(LetterColours)): # Starting the loop that checks what lowercase letter the pixel corresponds to.
            if TargetImage.getdata(band=0)[Count] == LetterColours[B] and TargetImage.getdata(band=1)[Count] == 0 and TargetImage.getdata(band=2)[Count] == 0: # Checking what lowercase letter that pixel corresponds to.
                OutText += Letters[B] # Adding the lowercase letter to the decrypted text.
    elif TargetImage.getdata(band=0)[Count] > 0 and TargetImage.getdata(band=1)[Count] == 0 and TargetImage.getdata(band=2)[Count] == 0: # Checking if the pixel corresponds to an uppercase letter.
        for B in range(len(LetterColours)): # # Starting the loop that checks what uppercase letter the pixel corresponds to.
            if TargetImage.getdata(band=0)[Count] == 0 and TargetImage.getdata(band=1)[Count] == LetterColours[B] and TargetImage.getdata(band=2)[Count] == 0: # Checking what uppercase letter that pixel corresponds to.
                OutText += Letters[B].upper() # Adding the lowercase letter to the decrypted text.
    else: # by process of elimination the character must be a symbol.
        for B in range(len(SymbolColours)): # Starting the loop that checks what symbol the pixel corresponds to.
            if TargetImage.getdata(band=0)[Count] == 0 and TargetImage.getdata(band=1)[Count] == 0 and TargetImage.getdata(band=2)[Count] == SymbolColours[B]: # Checking what Symbol that pixel corresponds to.
                OutText += Symbols[B] # Adding the lowercase letter to the decrypted text.

print("\nPROGRAMME:\n    Decrypted text reads:\n    " + OutText) # Informing the user what the decrypted text reads.