from random import randint
import random
import time

agamble = 1
bgamble = 1
player1 = 0
player2 = 0
player = 1
while(player1 != 100 and player2 != 100):
  if player == 1:
    while(agamble == 1):
      roll = randint(1,6)
      roll2 = randint(1,6)
      total = roll + roll2
      if roll == 1:
        total = 0
        if roll2 == 1:
          player1 = 0
      if roll2 == 1:
        total = 0
        if roll == 1:
          player1 = 0
      if roll != 1 and roll2 != 1:
        print("You are currently at " + str(player1) + " and you just rolled a total of " + str(total))
        g = input("gamble or bank? ")
        if g == "bank":
          player1 = player1 + total
          print("you are now at " + str(player1))
          agamble = 0
          time.sleep(0.1)
          player = 2
        else:
          agamble = 1
      else:
        print("u got at least 1 1")
        player = 2
  
  else:
    while(bgamble == 1):
      roll = randint(1,6)
      roll2 = randint(1,6)
      total = roll + roll2
      if roll == 1:
        total = 0
        if roll2 == 1:
          player2 = 0
      if roll2 == 1:
        total = 0
        if roll == 1:
          player2 = 0
      if roll != 1 and roll2 != 1:
        print("You are currently at " + str(player2) + " and you just rolled a total of " + str(total))
        g = input("gamble or bank? ")
        if g == "bank":
          player2 = player2 + total
          print("you are now at " + str(player2))
          bgamble = 0
          time.sleep(0.1)
          player = 1
        else:
          bgamble = 1
      else:
        print("u got at least 1 1")
        player = 1
