while (True):
    word = input("enter word: ")
    word = word.upper()
    shift = input("code or decode: ")
    if shift == "code":
        shift = 13
    elif shift == "decode":
        shift = -13
    elif shift != "code" and shift != "decode":
        print("no make sense")

    string = (word)
    wholeword = []

    for letter in string:

        value = ord(letter)
        value = int(value) + int(shift)
        if value > 90:
            value = value - 26
        if value < 64:
            value = value + 26

        newLetter = chr(value)
        print(str(newLetter), end="")

        wholeword.append(newLetter)

    print("")
    print(wholeword)
    print("")
