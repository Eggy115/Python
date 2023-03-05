a = input("what currency are you converting to? ")
b = float(input("how many great british pound stirling do you have?"))
currency = ["EUR", "USD", "CNY", "AUD", "EGP", "ZAR", "KRW", "UAH"]
rate = [1.14, 1.14, 8.62, 1.78, 27.82, 20.25, 1569.43, 42.01]
curtype = currency.index(a)
c = rate[curtype]
d = b * c
print(d)
