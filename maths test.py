from random import randint
import random
import time
score = 0

for i in range(10):
    roll = randint(1,10)
    roll2 = randint(1,10)
    answer = roll * roll2
    answer = int(answer)
    print(str(roll) + "*" + str(roll2) + " ")
  
    q = input("")
    q = int(q)
    if q == answer:
      score = score + 1
      print("yes\n")
    else:
      print("no\n")
  
print(str(score) + "/10")
