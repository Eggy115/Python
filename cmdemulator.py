import os
import time
while(True):
  cmd = input(str(str(os.getcwd()) +  " | " + time.ctime().upper() + " | Prompt> "))
  os.system(str(cmd))
