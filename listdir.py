import os
string = os.listdir()
drive = os.getcwd()
drive = drive.replace("\\","/")
for i in range(len(string)):
        dir = os.path.isfile(str(drive) + "/" + string[i])
        file_size = os.path.getsize(str(drive) + "/" + string[i])
        gap = "                                                        "
        gap = gap[:-int(len(string[i]))]
        w = string[i].split(".")
        if dir == True:
                sec = "                         "
                sec = sec[:-int(len(w[-1]))]
                print(string[i] + gap + w[-1].upper() + " FILE" + str(sec) + str(file_size) + " bytes")
        else:
                print(string[i] + gap + "DIRECTORY")
input()

