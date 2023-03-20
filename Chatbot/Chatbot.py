import time
import os
import threading
from random import randint
from difflib import SequenceMatcher
from getpass import getpass
from math import *
import base64
text_file = open("wordlist.txt", "r")
lines = open('wordlist.txt').read().splitlines() 
donot = ["Make sure you","Never","Do not","","Start by","If you can,","Start to","Immediately","Cancel the action of"]
colours = ["red","yellow","brown","blue"]
empty = ["...","why you send blank message"] 	

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

os.system("title AI Chatbot")
print("""================================================
            AI Chatbot [BORGERTRON]
              Created by Eggy115
                   v1.0.0
================================================""")

while(True):
  inputs = input("\nYou: ")
  
  if inputs == "lmao":
    message = "lmao"

  elif inputs == "":
    message = empty[0,(len(empty)-1)]

  elif similar("my name is",str(inputs)) > 0.5:
    name = inputs.split()
    namel = len(name)
    name = name[len(name) - 1]
    message = name

  elif "name" in inputs:
    message = "Hello, " + name

  elif "hello" in inputs or "hi" in inputs:
    message = "Hello"

  elif "cook" in inputs or "make" in inputs:
    message = str(donot[randint(0,(len(donot)-1))]) + """ lightly roast the """ + str(lines[randint(0,370102)]) + """ in a wide pan until it get a golden """ + str(colours[randint(0,(len(donot)-1))]) + """color.
Wait for the """ + inputs.split()[len(inputs.split()) - 1] + """ to completely cool down.
""" + str(donot[randint(0,(len(donot)-1))]) + """ mix """ + inputs.split()[len(inputs.split()) - 1] + """ together, starting from the """ + str(lines[randint(0,370102)]) + """ and """ + inputs.split()[len(inputs.split()) - 1] + """ while adjusting the Sumac (optionally citric acid) and salt to taste.
Store in an airtight jar or container."""

  elif inputs.startswith("when was"):
    message = (str(inputs)[9:] + " was on " + str(randint(1,28)) + "/" + str(randint(1,12)) + "/" + str(randint(1000,2024))).capitalize() + "."

  elif inputs.startswith("top"):
    lel = inputs.split()
    message = "\n"
    for i in range(int(lel[1])):
      message = message + ("\nNumber " + str(i + 1) + ": " + lines[randint(0,370102)].capitalize() + " " + str(inputs)[7:])

  else:
    message = lines[randint(0,370102)].capitalize()
    for i in range(randint(1,20)):
      random = randint(1,10)
      if random == 1:
        message = message + ","
      message = message + " " + lines[randint(0,370102)]
    message = message + "."

  random = randint(1,10)
  if random == 1:
    message = message[:-(randint(1,len(message)))] + "- I forgor"

  print("\nAI: " + message)