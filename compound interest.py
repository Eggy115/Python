bal = input("current balance: ")
inr = input("interest (%): ")
des = input("desired balance: ")
year = 0
bal = int(bal)
inr = int(inr)
des = int(des)
while(bal < des):
  year = year + 1
  bal = bal + (bal * (inr / 100))
  print("\nyear " + str(year))
  print("bal " + str(bal))
  bal = int(bal)
  inr = int(inr)
  des = int(des)
