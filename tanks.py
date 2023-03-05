player = 1
player1 = []
player2 = []
win = 0

print("this is tanks\nwhen asked to put tank put number then number between 0 and 7 eg 56\n")

print("PLAYER 1")
for i in range(10):
  a = int(input("where put TANK "))
  if a > 77 or a < 0:
    print("no. tank removed.")
  else:
    if a in player1:
      print("no. tank removed.")
    else:
      player1.append(int(a))
print(player1)

print("\nPLAYER 2")
for i in range(10):
  a = int(input("where put TANK "))
  if a > 77 or a < 0:
    print("no. tank removed.")
  else:
    if a in player2:
      print("no. tank removed.")
    else:
      player2.append(int(a))
print(player2)

for i in range(50):
  print("\n")

while(win == 0):
  if player == 1:
    print("\nPLAYER 1")
    des = int(input("where do uwant to destory "))
    if int(des) in player2:
      player2.remove(des)
      print("u got their tank. they now have " + str(len(player2)) + " tanks")
      if len(player2) == 0:
        print("player 1 win")
        win = 1
    player = 2

  if player == 2:
    if win == 1:
      print("")
    else:  
      print("\nPLAYER 2")
      des = int(input("where do uwant to destory "))
      if int(des) in player1:
        player1.remove(des)
        print("u got their tank. they now have " + str(len(player1)) + " tanks")
        if len(player1) == 0:
          print("player 2 win")
          win = 1
      player = 1 
