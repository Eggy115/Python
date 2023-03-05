board = []
loc = 0
board.insert(int(loc), "O")
for i in range(100):
  board.append("x")

def bprint():
  var = 0
  for i in range(10):
    for i in range(10):
      print(board[i + var], "", flush=True, end="")
    print("")
    var = var + 10
bprint()

while(True):
  a = input("CONTROL:")
  if a == "d":
    del board[int(loc)]
    board.insert(int(loc) + 1, "O")
    loc = loc + 1
    bprint()
  if a == "a":
    del board[int(loc)]
    board.insert(int(loc) - 1, "O")
    loc = loc - 1
    bprint()
  if a == "w":
    del board[int(loc)]
    board.insert(int(loc) - 10, "O")
    loc = loc - 10
    bprint()
  if a == "s":
    del board[int(loc)]
    board.insert(int(loc) + 10, "O")
    loc = loc + 10
    bprint()   
