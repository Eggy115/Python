a = input("enter word: ")
word = a.upper()
leng = len(word)
print(word)
test = list(word)
print(test)
score = 0

print("")
counter = 0
while counter !=leng:
  print(test[counter], counter)

  if test[counter] == "E":
    score = score + 1
  if test[counter] == "A":
    score = score + 2
  if test[counter] == "R":
    score = score + 3
  if test[counter] == "I":
    score = score + 4
  if test[counter] == "O":
    score = score + 5
  if test[counter] == "T":
    score = score + 6
  if test[counter] == "N":
    score = score + 7
  if test[counter] == "S":
    score = score + 8
  if test[counter] == "L":
    score = score + 9
  if test[counter] == "C":
    score = score + 10
  if test[counter] == "U":
    score = score + 11
  if test[counter] == "D":
    score = score + 12 
  if test[counter] == "P":
    score = score + 13
  if test[counter] == "M":
    score = score + 14
  if test[counter] == "H":
    score = score + 15
  if test[counter] == "G":
    score = score + 16
  if test[counter] == "B":
    score = score + 17
  if test[counter] == "F":
    score = score + 18
  if test[counter] == "Y":
    score = score + 19
  if test[counter] == "W":
    score = score + 20
  if test[counter] == "K":
    score = score + 21
  if test[counter] == "V":
    score = score + 22
  if test[counter] == "X":
    score = score + 23
  if test[counter] == "Z":
    score = score + 24
  if test[counter] == "J":
    score = score + 25 
  if test[counter] == "Q":
    score = score + 26  
    
  counter = counter + 1

print("SCORE:", score)
