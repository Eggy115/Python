var = str(input())
ana = str(sorted([*str(var)]))
text_file = open("words.txt", "r")
lines = open('words.txt').read().splitlines() 
for counter in range(370103):
        if ana == str(sorted([*str(lines[counter])])):
                print("\n" + str(ana) + "\n" + str(lines[counter]) + "\n")
text_file.close
input("")
