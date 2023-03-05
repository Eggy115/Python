player1 = 501
player2 = 501
player = 1
print("NEW GAME\n")

while(player1 != 0 and player2 != 0):

  if player == 1:  
    a = int(input("PLAYER1 score: " + str(player1) + " | enter total from 3 darts: "))
    player1 = int(player1)
    if player1 - a > 0:
      player1 = player1 - a
      player = 2
    else: 
      player1 = 0
      player2 = 0
      print("PLAYER1 win")

  if player == 2:  
    a = int(input("PLAYER2 score: " + str(player2) + " | enter total from 3 darts: "))
    player2 = int(player2)
    if player2 - a > 0:
      player2 = player2 - a
      player = 1
    else: 
      player1 = 0
      player2 = 0
      print("PLAYER2 win")
