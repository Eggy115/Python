temp = input("temp? ")

if int(temp) > 0 and int(temp) < 100:
  print("no")
else:
    if int(temp) > 99:
        print("boil")
    if int(temp) < 1:
        print("frozen")
