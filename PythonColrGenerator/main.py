from colr import Colr as C
from random import randint
colours = ['FF0000','FF1100','FF2200','FF3300','FF4400','FF5500','FF6600','FF7700','FF8800','FF9900','FFAA00','FFBB00','FFCC00','FFDD00','FFEE00','FFFF00','EEFF00','DDFF00','CCFF00','BBFF00','AAFF00','99FF00','88FF00','77FF00','66FF00','55FF00','44FF00','33FF00','22FF00','11FF00','00FF00','00FF11','00FF22','00FF33','00FF44','00FF55','00FF66','00FF77','00FF88','00FF99','00FFAA','00FFBB','00FFCC','00FFDD','00FFEE','00FFFF','00EEFF','00DDFF','00CCFF','00BBFF','00AAFF','0099FF','0088FF','0077FF','0066FF','0055FF','0044FF','0033FF','0022FF','0011FF','0000FF','1100FF','2200FF','3300FF','4400FF','5500FF','6600FF','7700FF','8800FF','9900FF','AA00FF','BB00FF','CC00FF','DD00FF','EE00FF','FF00FF','FF00EE','FF00DD','FF00CC','FF00BB','FF00AA','FF0099','FF0088','FF0077','FF0066','FF0055','FF0044','FF0033','FF0022','FF0011']
rainboot = 0
def colour(string):
    num = 0
    var = 0
    for char in string:
            var = var + 1
            if var % 190 == 0:
                num = 0
            if char == "\n":
                    num = 0
                    var = 0
                    if rainboot == 1:
                        colours.append(str(colours[0]))
                        colours.pop(0)  
            colour = colours[num]

            print(C().hex(colour, char), end="", flush=True)
            if char == "ㅤ":
                    num = num
            else:
                    num = num + 1    
            if (int(num) + 1) > int(len(colours)):
                    num = 0
    if rainboot == 1:
        colours.append(str(colours[0]))
        colours.pop(0)                      
def test():
    colour("""\nLorem ipsum dolor sit amet, consectetur adipiscing elit.
Nullam dapibus est sed tincidunt tincidunt. 
Suspendisse malesuada sagittis enim, vel porta velit maximus vel. 
Maecenas pulvinar fermentum magna. Proin sed nunc ac ante condimentum elementum id in est. 
Pellentesque sollicitudin lorem quis felis congue, sit amet pretium libero vehicula. Curabitur id ornare arcu. 
Nunc cursus tempor ullamcorper. Vestibulum in sem neque. Curabitur porttitor lobortis varius. 
Praesent felis risus, tincidunt tincidunt pulvinar id, tempor a purus. 
Nulla bibendum tellus ac tincidunt volutpat. 
Donec vehicula leo ut lacus facilisis ornare. 
Vestibulum vel nisi arcu.\n\n""")

def matrix():
    while(True):
        string = "0"
        for i in range(188):
            string = string + str(randint(0,1))
        colour(string)

def help():
    colour("""\nfrom main import *

help()
test()
colour(\"text\")
matrix()\n\n""")
