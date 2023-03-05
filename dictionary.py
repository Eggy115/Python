a = input("what do u want to find: ")
text_file = open("wordlist.txt", "r")
lines = open('wordlist.txt').read().splitlines() 
counter = 0
found = False
while found == False and counter !=370103:
  if a == lines[counter]:
    print(lines[counter] + " is word")
    print("also:", lines[counter + 1], lines[counter - 1], lines[counter + 2], lines[counter - 2])
    found = True
  counter = counter + 1
