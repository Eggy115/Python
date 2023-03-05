from random import randint

player1 = 0
player2 = 0
points = 0
player = 1
while (player1 < 100 and player2 < 100):
  if player == 1:
    print("player1", player1)
    input("")
  if player == 2:
    print("player2", player2)
    input("")
  points = 0
  piga = randint(1, 5)
  pigb = randint(1, 5)

  if piga == 1 and pigb == 1:
    print("sider 1")
    points = 1

  if piga == 2 and pigb == 2:
    print("sider 1")
    points = 1

  if piga == 1 and pigb == 2:
    print("pigout")
    player1 = 0

  if piga == 2 and pigb == 1:
    print("pigout")
    player1 = 0

  if piga == 3 and pigb == 3:
    print("double trotter 20")
    points = 20

  if piga == 3 and pigb == 1:
    print("trotter 5")
    points = 5

  if piga == 3 and pigb == 2:
    print("trotter 5")
    points = 5

  if piga == 1 and pigb == 3:
    print("trotter 5")
    points = 5

  if piga == 2 and pigb == 3:
    print("trotter 5")
    points = 5

  if piga == 4 and pigb == 4:
    print("double snouter 20")
    points = 20

  if piga == 5 and pigb == 5:
    print("double razorback 20")
    points = 20

  if piga == 4 and pigb == 1:
    print("snouter 5")
    points = 5
  if piga == 4 and pigb == 2:
    print("snouter 5")
    points = 5
  if piga == 4 and pigb == 3:
    print("snouter 5")
    points = 5
  if piga == 1 and pigb == 4:
    print("snouter 5")
    points = 5
  if piga == 2 and pigb == 4:
    print("snouter 5")
    points = 5
  if piga == 3 and pigb == 4:
    print("snouter 5")
    points = 5

  if piga == 5 and pigb == 1:
    print("razorback 5")
    points = 5
  if piga == 5 and pigb == 2:
    print("razorback 5")
    points = 5
  if piga == 5 and pigb == 3:
    print("razorback 5")
    points = 5
  if piga == 1 and pigb == 5:
    print("razorback 5")
    points = 5
  if piga == 2 and pigb == 5:
    print("razorback 5")
    points = 5
  if piga == 3 and pigb == 5:
    print("razorback 5")
    points = 5
  if piga == 4 and pigb == 5:
    print("razorback 5")
    points = 5
  if piga == 5 and pigb == 4:
    print("razorback 5")
    points = 5

  if player == 1:
    player1 = player1 + points
    y = input("go again? y/n")
    if y == "n":
      player = 2
    else:
      player = 1

  else:
    player2 = player2 + points
    y = input("go again? y/n")
    if y == "n":
      player = 1
    else:
      player = 2
