# REQUIRES WORDS.TXT

a = input("what do u want to find: ")
text_file = open("words.txt", "r")
lines = open('words.txt').read().splitlines() 
counter = 0
found = False
while found == False and counter !=370103:
  if a == lines[counter]:
    print(lines[counter] + " is word")
    print("also:", lines[counter + 1], lines[counter - 1], lines[counter + 2], lines[counter - 2])
    found = True
  counter = counter + 1
