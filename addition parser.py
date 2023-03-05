calc = input("enter calculation: ")
calc = calc.split("+")
l = len(calc)
print(calc, l)
c = 0
answer = 0
while(c < l):
  answer = answer + int(calc[c])
  c = c + 1

print(answer)
