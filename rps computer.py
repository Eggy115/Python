from random import randint
import random

player1 = 0
player2 = 0
score = 0
total = 0
cscore = 0
while (score < 10):
  comp = randint(1, 3)
  if comp == 1:
    comp = "rock"
  if comp == 2:
    comp = "paper"
  if comp == 3:
    comp = "scissors"

  player = input("rock paper or scissors: ")
  if player == "rock" or player == "paper" or player == "scissors":

    total = total + 1
    if player == "rock":
      if comp == "rock":
        print("draw")
      if comp == "paper":
        print("lose")
        cscore = cscore + 1
      if comp == "scissors":
        print("win")
        score = score + 1

    if player == "paper":
      if comp == "rock":
        print("win")
        score = score + 1
      if comp == "paper":
        print("draw")
      if comp == "scissors":
        print("lose")
        cscore = cscore + 1

    if player == "scissors":
      if comp == "rock":
        print("lose")
        cscore = cscore + 1
      if comp == "paper":
        print("win")
        score = score + 1
      if comp == "scissors":
        print("draw")

  else:
    print("no")
print("you won 10. computer won", cscore, "total was:", total)
