try:
        password = input()
        print("\nPassword: \"" + password + "\"\n\nthings wrong with your password\n")
        if len(password) < 20:
                print("- too short\n")
        chars = [*str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
        detectcaps = 0
        for i in chars:
                if i in password:
                        detectcaps = 1
        if detectcaps == 0:
                print("- doesnt contain caps\n")

        newchars = [*str(str("ABCDEFGHIJKLMNOPQRSTUVWXYZ").lower())]
        detectlow = 0
        for id in newchars:
                if id in password:
                        detectlow = 1
        if detectlow == 0:
                print("- doesnt contain lowercase\n")
        
        newnewchars = [*str(str("0123456789").lower())]
        detectnum = 0
        for ic in newnewchars:
                if ic in password:
                        detectnum = 1
        if detectnum == 0:
                print("- doesnt contain numbers\n")

        newnewnewchars = [':', ';', '@', '#', '~', '/', '?', '.', ',','<','>','!', '$', '%', '^','&', '*', '(', ')', '{', '}', '[', ']', '-', '+', '=', '_','\\', '|', '`', '"']
        detectsym = 0
        for ig in newnewnewchars:
                if ig in password:
                        detectsym = 1
        if detectsym == 0:
                print("- doesnt contain symbols\n")
        input("")
except:
        print("no worky")
