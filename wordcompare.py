word = input("word: ")
word = word.upper()
list = []
for letter in word:
  list.append(letter)
print(list)

word2 = input("wordcompare: ")
word2 = word2.upper()
a = 0
for i in range(len(word)):
  if list[int(a)] in word2:
    print("invalid")
    pass
  a = a + 1
