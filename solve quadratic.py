import math

a = int(input("a "))
b = int(input("b "))
c = int(input("c "))
answer = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
print(answer)
answer = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
print(answer)
