import math
from decimal import *
import decimal

change = []
p = Decimal(input("enter money in pounds: "))

tpound = p / 2
print(p, "/ 2 =", tpound)
a = math.floor(tpound)
print(a, "x £2")
p = p - int(a) - int(a)
print(p, "left to go\n")
change.append(a)

pound = p / 1
print(p, "/ 1 =", pound)
a = math.floor(pound)
print(a, "x £1")
p = p - int(a)
print(p, "left to go\n")
change.append(a)

fifty = p / Decimal('0.5')
print(p, "/ 0.50 =", fifty)
a = math.floor(fifty)
print(a, "x £0.50")
p = p - (Decimal(a) / 2)
print(p, "left to go\n")
change.append(a)

ten = p / Decimal('0.1')
print(p, "/ 0.1 =", ten)
a = math.floor(ten)
print(a, "x £0.10")
p = p - (Decimal(a) / 10)
print(p, "left to go\n")
change.append(a)

five = p / Decimal('0.05')
print(p, "/ 0.05 =", five)
a = math.floor(five)
print(a, "x £0.05")
p = p - (Decimal(a) / 20)
print(p, "left to go\n")
change.append(a)

two = p / Decimal('0.02')
print(p, "/ 0.02 =", two)
a = math.floor(two)
print(a, "x £0.02")
p = p - (Decimal(a) / 50)
print(p, "left to go\n")
change.append(a)

one = p / Decimal('0.01')
print(p, "/ 0.01 =", one)
a = math.floor(one)
print(a, "x £0.01")
p = p - (Decimal(a) / 100)
print(p, "left to go\n")
change.append(a)

print(change)
