list = ["0","1","2","3","4","5","6","7","8",]
def table():
  print("\n")
  print(list[0] + " " + list[1] + " " + list[2])
  print(list[3] + " " + list[4] + " " + list[5])
  print(list[6] + " " + list[7] + " " + list[8])
  print("\n")
table()
def check():
  if list[0] == list[1] and list[0] == list[2]:
    if list[0] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()
  if list[3] == list[4] and list[3] == list[5]:
    if list[3] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()
  if list[6] == list[7] and list[6] == list[8]:
    if list[6] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()

  if list[0] == list[3] and list[0] == list[6]:
    if list[0] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()
  if list[1] == list[4] and list[1] == list[7]:
    if list[1] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()
  if list[2] == list[5] and list[2] == list[8]:
    if list[2] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()

  if list[0] == list[4] and list[0] == list[8]:
    if list[0] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()
  if list[2] == list[4] and list[2] == list[6]:
    if list[2] == "X":
      print("cross win")
      exit()
    else:
      print("nought win")
      exit()

player = 0
while(True):
  if player == 0:
    a = input("PLACE CROSS: ")

    list.remove(str(a))
    list.insert(int(a), "X")
    table()
    check()
    player = 1
  else:
    a = input("PLACE NOUGHT: ")
    list.remove(str(a))
    list.insert(int(a), "O")
    table()
    check()
    player = 0
