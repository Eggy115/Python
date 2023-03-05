from random import randint
import threading
import time

visual = ("""
battleships boarddddd
  0 1 2 3 4 5 6 7 8 9
0 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
1 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
2 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■   
3 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
4 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
5 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
6 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
7 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
8 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
9 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
""")
print(visual)

board = []
roboboard = []
count = 4

while (count > 0):
  b = input("place battleship ")

  try:
    int(b)
    if b in board:
      print("battleship already there")
    else:
      board.append(b)
      count = count - 1

  except:
    print("not a number")

count = 4
while (count > 0):
  comp1 = randint(0, 9)
  comp2 = randint(0, 9)
  b = str(comp1) + str(comp2)
  if b in roboboard:
    pass
  else:
    roboboard.append(b)
    count = count - 1

print("you", board)
print("robot", roboboard)
end = 1
comptarget = 00
while(end == 1):

  fire = input("shoot ")
  if fire in roboboard:
    roboboard.remove(fire)
    print(roboboard)
    print("you hit")
  
  if comptarget == 00:
    comp1 = randint(0, 9)
    comp2 = randint(0, 9)
    comptarget = str(comp1) + str(comp2)
  print(comptarget)
  if comptarget in board:
    board.remove(comptarget)
    print(board)
    print("you got hit")
    comptarget = int(comptarget) + 1
  else:
    comptarget = 00
    
  if roboboard == []:
    print("you win")
    end = 0
  if board == []:
    print("you lose")
    end = 0
