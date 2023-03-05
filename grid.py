def gr():
  grid_size = 3
  return grid_size
grid_size = 3
game = ' '
c = 65
print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size):
    print( i+1 , end='')
    for j in range(grid_size):
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")
  
a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
one = a[:b]
two = a[c:]
one = int(one) - 1
two = int(two) - 1

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i == two:
        print(f"| x ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
three = a[:b]
four = a[c:]
three = int(three) - 1
four = int(four) - 1

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
five = a[:b]
six = a[c:]
five = int(five) - 1
six = int(six) - 1

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four or j == five and i==six:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
        if j == five and i==six:
          print(f"| x ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
seven = int(a[:b]) - 1
eight = int(a[c:]) - 1 

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four or j == five and i==six or j==seven and i==eight:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
        if j == five and i==six:
          print(f"| x ", end='')
        if j == seven and i==eight:
          print(f"| o ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
nine = int(a[:b]) - 1
ten = int(a[c:]) - 1 

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four or j == five and i==six or j==seven and i==eight or j==nine and i==ten:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
        if j == five and i==six:
          print(f"| x ", end='')
        if j == seven and i==eight:
          print(f"| o ", end='')
        if j==nine and i==ten:
          print(f"| x ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
eleven = int(a[:b]) - 1
twelve = int(a[c:]) - 1 

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four or j == five and i==six or j==seven and i==eight or j==nine and i==ten or j==eleven and i==twelve:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
        if j == five and i==six:
          print(f"| x ", end='')
        if j == seven and i==eight:
          print(f"| o ", end='')
        if j==nine and i==ten:
          print(f"| x ", end='')
        if j==eleven and i==twelve:
          print(f"| o ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
thirteen = int(a[:b]) - 1
fourteen = int(a[c:]) - 1 

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four or j == five and i==six or j==seven and i==eight or j==nine and i==ten or j==eleven and i==twelve or j==thirteen and i==fourteen:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
        if j == five and i==six:
          print(f"| x ", end='')
        if j == seven and i==eight:
          print(f"| o ", end='')
        if j==nine and i==ten:
          print(f"| x ", end='')
        if j==eleven and i==twelve:
          print(f"| o ", end='')
        if j==thirteen and i==fourteen:
          print(f"| x ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
fifteen = int(a[:b]) - 1
sixteen = int(a[c:]) - 1 

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four or j == five and i==six or j==seven and i==eight or j==nine and i==ten or j==eleven and i==twelve or j==thirteen and i==fourteen or j==fifteen and i==sixteen:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
        if j == five and i==six:
          print(f"| x ", end='')
        if j == seven and i==eight:
          print(f"| o ", end='')
        if j==nine and i==ten:
          print(f"| x ", end='')
        if j==eleven and i==twelve:
          print(f"| o ", end='')
        if j==thirteen and i==fourteen:
          print(f"| x ", end='')
        if j==fifteen and i==sixteen:
          print(f"| o ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

a = str(input("what are your co-ords? "))
s = str(",")
b = a.find(s)
for i in a:
  c = b+1
seventeen = int(a[:b]) - 1
eighteen = int(a[c:]) - 1 

print(f"  ", end='')
for j in range(grid_size):
     print(f"| {j+1} ", end='')
print("| ")
print((grid_size*4+4)*"-")

for i in range(grid_size): 
    print( i+1 , end='')
    for j in range(grid_size):
      if j == one and i==two or j == three and i == four or j == five and i==six or j==seven and i==eight or j==nine and i==ten or j==eleven and i==twelve or j==thirteen and i==fourteen or j==fifteen and i==sixteen or j==seventeen and i==eighteen:
        if j == one and i==two:
          print(f"| x ", end='')
        if j == three and i == four:
          print(f"| o ", end='')
        if j == five and i==six:
          print(f"| x ", end='')
        if j == seven and i==eight:
          print(f"| o ", end='')
        if j==nine and i==ten:
          print(f"| x ", end='')
        if j==eleven and i==twelve:
          print(f"| o ", end='')
        if j==thirteen and i==fourteen:
          print(f"| x ", end='')
        if j==fifteen and i==sixteen:
          print(f"| o ", end='')
        if j==seventeen and i==eighteen:
          print(f"| x ", end='')
      else:
        print(f"| {game} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")
