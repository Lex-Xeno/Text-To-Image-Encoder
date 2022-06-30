while(1):
  Programme = int(input("\nPROGRAMME:\n    What programme would you like to run\n    Text To Image[1]\n    Image To Text[2]\nUSER:\n    "))
  if Programme == 1:
    import TextToImage
    break
  elif Programme == 2:
    import ImageToText
    break
  else:
    print("\nPROGRAMME:\n    That is not a valid input")