year = 0
bal = float(input("enter balance: "))
inr = float(input("enter interest: "))
amou = int(input("enter how many years: "))
print("\nOriginal Price | £" + str(bal) + "\nInterest Rate  | " + str(inr) + "%")
for i in range(int(amou + 1)):
        print("Year " + str(year) + "	| Price £" + str(bal))
        year = year + 1
        bal = bal + (bal * (inr / 100))
        bal = float(bal)
        inr = float(inr)
input("\n")
