#setup
import time
from random import randint
player = []
dealer = []
playerv = 0
dealerv = 0
playerl = 0
dealerl = 0
counter = 0

#deal two random cards
for i in range(2):
    newc = randint(1,13)
    player.append(newc)    
    newc = randint(1,13)
    dealer.append(newc)

#show all cards, length
playerl = len(player)
dealerl = len(dealer)
print("player", player, playerl)
print("dealer", dealer, dealerl)
print("")
if 1 == 1:
  counter = 0
  playerv = 0
  for i in range (playerl):
    if player[counter] == 1:
      print("ace 1")
      playerv = playerv + 1
    elif player[counter] == 13:
      print("king 10")
      playerv = playerv + 10
    elif player[counter] == 12:
      print("queen 10")
      playerv = playerv + 10
    elif player[counter] == 11:
      print("jack 10")
      playerv = playerv + 10
    elif player[counter] > 1 and player[counter] < 11:
      print("any other card", player[counter])
      playerv = playerv + player[counter]    
    counter = counter + 1
  print("your current value is", playerv)

print("")
if 1 == 1:
  counter = 0
  dealerv = 0
  for i in range (dealerl):
    if dealer[counter] == 1:
      print("ace 1")
      dealerv = dealerv + 1
    elif dealer[counter] == 13:
      print("king 10")
      dealerv = dealerv + 10
    elif dealer[counter] == 12:
      print("queen 10")
      dealerv = dealerv + 10
    elif dealer[counter] == 11:
      print("jack 10")
      dealerv = dealerv + 10
    elif dealer[counter] > 1 and dealer[counter] < 11:
      print("any other card", dealer[counter])
      dealerv = dealerv + dealer[counter]    
    counter = counter + 1
  print("dealer current value is", dealerv)

print("")

sw = input("stick or twist? ")
if sw == "stick":

  print("your current value is", playerv)
  print("dealer value is", dealerv)
  if playerv == dealerv:
    print("draw")
  if playerv > dealerv:
    print("player win")
  if dealerv > playerv:
    print("dealer win")
    
if sw == "twist":
  newc = randint(1,13)
  player.append(newc)   
  playerl = len(player)
  dealerl = len(dealer)
  print("player", player, playerl)
  print("dealer", dealer, dealerl)
  print("")
  counter = 0
  playerv = 0
  for i in range (playerl):
    if player[counter] == 1:
      print("ace 1")
      playerv = playerv + 1
    elif player[counter] == 13:
      print("king 10")
      playerv = playerv + 10
    elif player[counter] == 12:
      print("queen 10")
      playerv = playerv + 10
    elif player[counter] == 11:
      print("jack 10")
      playerv = playerv + 10
    elif player[counter] > 1 and player[counter] < 11:
      print("any other card", player[counter])
      playerv = playerv + player[counter]    
    counter = counter + 1
  print("your current value is", playerv)
  print("dealer value is", dealerv)

  if playerv > 21:
    print("youwent bust")
    exit()
  if playerv == dealerv: 
    print("draw")
  if playerv > dealerv:
    print("player win")
  if dealerv > playerv:
    print("dealer win")
