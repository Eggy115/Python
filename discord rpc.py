from pypresence import Presence
import time
import webbrowser
import tkinter
from tkinter import *

start=time.time()

print("RPC Activated")
print("Created by Eggy115")

rpc = Presence("enter RPC ID here")
rpc.connect()
rpc.update(buttons=[{"label": "Label", "url": "https://github.com/"},{"label": "Label", "url": "https://github.com/"}],state="State",details="Details",large_image="large_image_here",small_image="small_image_here",large_text="large text",small_text="small text",start=start)

while(True):
        time.sleep(3)
