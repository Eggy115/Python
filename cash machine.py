money = 231
a = int(input("how much would you like to withdraw? current balance = 231",))
b = a % 10
if a < 231: 
  if b == 0:
    money = money - a
    print(money)
  else:
    a = a + 10 - b
    print("can only withdraw tens or 20s, withdrawing ", a, "instead")
    money = money - a
    print(money)
