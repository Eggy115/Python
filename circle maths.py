dia = input("dia? ")
arca = input("arca? ")

r = int(dia) / 2
a = int(r) * int(r) * 3.14
c = int(dia) * 3.14
arc = int(c) * int(arca)
arc = arc / 360

print("radius:", int(r))
print("area", int(a))
print("circ:", int(c))
print("arcl:", int(arc))
