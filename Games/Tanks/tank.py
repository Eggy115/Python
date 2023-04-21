def begseq():
  global player1
  global player2
  print("HELLO - WELCOME TO TANKS, A GAME FOR TWO PLAYERS")
  print("PLAYER ONE PLEASE ENTER WHAT YOU WISH TO BE KNOWN AS")
  player1 = input()
  print("PLAYER TWO PLEASE ENTER WHAT YOU WISH TO BE KNOWN AS")
  player2 = input()
  print("THE GAME WILL BE PLAYED ON A 9X9 GRID")

repa = 1

def howmanytanksp1():
  global tnk
  tnk = 0
  for i in game:
    if i != " ":
      tnk = tnk + 1
def howmanytanksp2():
  global tnk
  tnk = 0
  for i in game:
    if i != " ":
      tnk = tnk + 1
      
      
def gamereset():
  global game
  game = [
  " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
  " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
  " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
  " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
  " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
  " ", " ", " ", " ", " ", " ", " "
]




def grid(game):
  print("   1   2   3   4   5   6   7   8   9")
  print("1"
        "|", game[1], "|", game[2], "|", game[3], "|", game[4], "|", game[5],
        "|", game[6], "|", game[7], "|", game[8], "|", game[9], "|")
  print("2"
        "|", game[10], "|", game[11], "|", game[12], "|", game[13], "|",
        game[14], "|", game[15], "|", game[16], "|", game[17], "|", game[18],
        "|")
  print("3"
        "|", game[19], "|", game[20], "|", game[21], "|", game[22], "|",
        game[23], "|", game[24], "|", game[25], "|", game[26], "|", game[27],
        "|")
  print("4"
        "|", game[28], "|", game[29], "|", game[30], "|", game[31], "|",
        game[32], "|", game[33], "|", game[34], "|", game[35], "|", game[36],
        "|")
  print("5"
        "|", game[37], "|", game[38], "|", game[39], "|", game[40], "|",
        game[41], "|", game[42], "|", game[43], "|", game[44], "|", game[45],
        "|")
  print("6"
        "|", game[46], "|", game[47], "|", game[48], "|", game[49], "|",
        game[50], "|", game[51], "|", game[52], "|", game[53], "|", game[54],
        "|")
  print("7"
        "|", game[55], "|", game[56], "|", game[57], "|", game[58], "|",
        game[59], "|", game[60], "|", game[61], "|", game[62], "|", game[63],
        "|")
  print("8"
        "|", game[64], "|", game[65], "|", game[66], "|", game[67], "|",
        game[68], "|", game[69], "|", game[70], "|", game[71], "|", game[72],
        "|")
  print("9"
        "|", game[73], "|", game[74], "|", game[75], "|", game[76], "|",
        game[77], "|", game[78], "|", game[79], "|", game[80], "|", game[81],
        "|")
  



def tanksam():
  global k
  global t
  global l
  global tankamount
  print("HOW MANY TANKS DO YOU WANT TO PLACE ON THIS BOARD")
  t = int(input())
  k = t
  tankamount = t
  l = t
  if t >= 81:
    print("YOU CANNOT HAVE MORE TANKS THAT AVAILIBLE SPACES")
    quit()
  else:
    playone()


def playerone():
  global v1
  global k
  print(player1,
        "PLEASE ENTER THE PLACE YOU WOULD LIKE TO PLACE A TANK - (11-99)")
  v1 = int(input())
  if 11 <= v1 <= 99:
    list = [int(i) for i in str(v1)]
    global letterv
    global numberv
    letterv = list[0]
    numberv = list[1]
    if letterv == 1:
      game[numberv] = "X"
    elif letterv == 2:
      game[numberv + 9] = "X"
    elif letterv == 3:
      game[numberv + 18] = "X"
    elif letterv == 4:
      game[numberv + 27] = "X"
    elif letterv == 5:
      game[numberv + 36] = "X"
    elif letterv == 6:
      game[numberv + 45] = "X"
    elif letterv == 7:
      game[numberv + 54] = "X"
    elif letterv == 8:
      game[numberv + 63] = "X"
    elif letterv == 9:
      game[numberv + 72] = "X"
    k = k - 1
    grid(game)
  else:
    print("THAT SPACE DOES NOT EXIST")


def playertwo():
  global v1
  global l
  print(player2,"PLEASE ENTER THE PLACE YOU WOULD LIKE TO PLACE A TANK - (11-99)")
  v1 = int(input())
  if 10 < v1 < 100:
    list = [int(i) for i in str(v1)]
    global letterv
    global numberv
    letterv = list[0]
    numberv = list[1]
    if letterv == 1:
      game[numberv] = "X"
    elif letterv == 2:
      game[numberv + 9] = "X"
    elif letterv == 3:
      game[numberv + 18] = "X"
    elif letterv == 4:
      game[numberv + 27] = "X"
    elif letterv == 5:
      game[numberv + 36] = "X"
    elif letterv == 6:
      game[numberv + 45] = "X"
    elif letterv == 7:
      game[numberv + 54] = "X"
    elif letterv == 8:
      game[numberv + 63] = "X"
    elif letterv == 9:
      game[numberv + 72] = "X"
    l = l - 1
    grid(game)
  else:
    print("THAT SPACE DOES NOT EXIST")


def playertwoguess():
  howmanytanksp1()
  tanksd = 0
  guesses = 0
  if tanksd == tnk:  
    print(player2, "YOU HAVE SUCCESFULLY DESTROYED", player1, "'s TANKS, IN",
          guesses, "GUESSES")
  print(player2, "YOU CAN NOW BEGIN TO GUESS WHERE", player1,
        "HAS PLACED THEIR", t, "TANKS - (11-99)")
  while tanksd != tnk:
    g = int(input())
    if 11 <= g <= 99:
      list = [int(i) for i in str(g)]
      global guess1
      global guess2
      guess1 = list[0]
      guess2 = list[1]
      if guess1 == 1:
        if game[guess2] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 2:
        if game[guess2 + 9] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 3:
        if game[guess2 + 18] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 4:
        if game[guess2 + 27] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 5:
        if game[guess2 + 36] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 6:
        if game[guess2 + 45] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 7:
        if game[guess2 + 54] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 8:
        if game[guess2 + 63] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 9:
        if game[guess2 + 72] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
    else:
      print("THAT GUESS IS INVALID")
  if tanksd == tnk:
    print(player1, "YOU HAVE SUCCESFULLY DESTROYED", player2, "'s TANKS, IN",
          guesses, "GUESSES")

def playeroneguess():
  howmanytanksp2()
  tanksd = 0
  guesses = 0
  if tanksd == tnk:  
    print(player1, "YOU HAVE SUCCESFULLY DESTROYED", player2, "'s TANKS, IN",
          guesses, "GUESSES")
  print(player1, "YOU CAN NOW BEGIN TO GUESS WHERE", player2,
        "HAS PLACED THEIR", t, "TANKS - (11-99)")
  while tanksd != tnk:
    g = int(input())
    if 11 <= g <= 99:
      list = [int(i) for i in str(g)]
      global guess1
      global guess2
      guess1 = list[0]
      guess2 = list[1]
      if guess1 == 1:
        if game[guess2] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 2:
        if game[guess2 + 9] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 3:
        if game[guess2 + 18] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 4:
        if game[guess2 + 27] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 5:
        if game[guess2 + 36] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 6:
        if game[guess2 + 45] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 7:
        if game[guess2 + 54] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 8:
        if game[guess2 + 63] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
      if guess1 == 9:
        if game[guess2 + 72] == "X":
          print("YOU HAVE DESTROYED A TANK")
          tanksd = tanksd + 1
          guesses = guesses + 1
        else:
          print("MISS")
          guesses = guesses + 1
    else:
      print("THAT GUESS IS INVALID")
  if tanksd == tnk:
    print(player2, "YOU HAVE SUCCESFULLY DESTROYED", player1, "'s TANKS, IN",
          guesses, "GUESSES")


def playone():
  while k > 0:
    playerone()
  if k == 0:
    enter = 100
    while enter > 0:
      print(" ")
      enter = enter - 1
  playertwoguess()
  gamereset()
  while l > 0:
    playertwo()
  if l == 0:
    enter = 100
    while enter > 0:
      print(" ")
      enter = enter - 1
  playeroneguess()
  gamereset()

def repa():
  print("WOULD YOU LIKE TO PLAY AGAIN? Y/N")
  global repa
  repe = input().upper
  if repe == "Y":
    repa = 1
  elif repe == "N":
    repa = 0
    print("THANK YOU FOR PLAYING")
    
  

  


def fullgame():
  gamereset()
  begseq()
  grid(game)
  tanksam()
  repa()

while repa != 0:
  fullgame()
