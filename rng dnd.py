from random import randint

print("""
================================================
            Random DND Thing
================================================
""")

places = ["forest","city","desert","school","cave","small village","jungle"]
items = ["computer","sword","pen"]
bad = ["n elephant"," troll"]
baddeath = [" and you get crushed by the elephant"," and the troll mutilates you"]
option = ["you run away","you spin around","you scream for help","you do a backflip","you yell at them","you charge at them and try to attack"]
goodending = [" and escape"," and confuse them"," and someone comes", " and theyre so impressed that they stop"," and they run away","and you successfully slay them"]
badending = [" but trip and fall"," but nothing happens"," but nobody comes"," but you land and break your neck"," but they dont care"," however you fail"]
inventory = []

print("you find yourself in a " + places[randint(0,6)] + " but you dont know how you got there")
inventory.append(items[randint(0,2)])
print("you have nothing but a " + inventory[0] + " in your pocket")
badrand = randint(0,1)
print("you look around and see a" + bad[badrand] + " in front of you")

print("\ndo you: ")
option1rand = randint(0,5)
option2rand = randint(0,5)
option3rand = randint(0,5)
option4rand = randint(0,5)
option1 = (option[option1rand])
option2 = (option[option2rand])
option3 = (option[option3rand])
option4 = (option[option4rand])
print("1 " + option1)
print("2 " + option2)
print("3 " + option3)
print("4 " + option4)
while(True):
  choice = input("")
  suc = randint(1,2)
  if suc == 1:
    if choice == "1":
      print(option1 + goodending[option1rand])
      break
    elif choice == "2":
      print(option2 + goodending[option2rand])
      break
    elif choice == "3":
      print(option3 + goodending[option3rand])
      break
    elif choice == "4":
      print(option4 + goodending[option4rand])
      break
    else:
      pass
  else:
    if choice == "1":
      print(option1 + badending[option1rand] + baddeath[badrand])
      exit()
    elif choice == "2":
      print(option2 + badending[option2rand] + baddeath[badrand])
      exit()
    elif choice == "3":
      print(option3 + badending[option3rand] + baddeath[badrand])
      exit()
    elif choice == "4":
      print(option4 + badending[option4rand] + baddeath[badrand])
      exit()
    else:
      pass
    
    
