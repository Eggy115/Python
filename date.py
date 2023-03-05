m = input("say month ")
m = int(m)
y = input("say year ")
y = int(y)
t = y % 4
if m == 1:
    print("jan 31")
if m == 2:
    if t == 0:
        print("feb 29")
    else:
        print("feb 28")
if m == 3:
    print("mar 31")
if m == 4:
    print("apr 30")
if m == 5:
    print("may 31")
if m == 6:
    print("jun 30")
if m == 7:
    print("jul 31")
if m == 8:
    print("aug 31")
if m == 9:
    print("sep 30")
if m == 10:
    print("oct 31")
if m == 11:
    print("nov 30")
if m == 12:
    print("dec 31")
