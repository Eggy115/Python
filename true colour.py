import time
from colr import Colr as C
A = 0
print("")
var = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
while(True):
        print(C(var + '''\r''', fore=(255, A, 0), back=(0, 0, 0)))
        A = A + 1
        time.sleep(0.01)
        if A == 255:
                break
A = 255
while(True):
        print(C(var + '''\r''', fore=(A, 255, 0), back=(0, 0, 0)))
        A = A - 1
        time.sleep(0.01)
        if A == 0:
                break
A = 0
while(True):
        print(C(var + '''\r''', fore=(0, 255, A), back=(0, 0, 0)))
        A = A + 1
        time.sleep(0.01)
        if A == 255:
                break
A = 255
while(True):
        print(C(var + '''\r''', fore=(0, A, 255), back=(0, 0, 0)))
        A = A - 1
        time.sleep(0.01)
        if A == 0:
                break  
A = 0
while(True):
        print(C(var + '''\r''', fore=(A, 0, 255), back=(0, 0, 0)))
        A = A + 1
        time.sleep(0.01)
        if A == 255:
                break     
input("\nDone\n")
