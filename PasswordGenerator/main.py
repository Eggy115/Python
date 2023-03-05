from random import *

try:
    lettercount = input("Length: ")
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8','9', ':', ';', '@', '#', '~', '/', '?', '.', ',','<','>', '!', '$', '%', '^','&', '*', '(', ')', '{', '}', '[', ']', '-', '+', '=', '_','\\', '|', '`', '"', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 'W', 'X', 'Y', 'Z']
    passw = ""

    for key in range(int(lettercount)):
        passw_letter = password[randint(0, int(len(password) - 1))]
        passw = str(passw_letter) + str(passw)

    print("\n" + passw)
except:
    print("\nFailed")
    
input("")