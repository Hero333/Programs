#! usr/bin/env python

import time,random
print("Hello and welcome to [insert text here]")
#time.sleep(5)
print("Unknown: Hello, Player")
print("Unknown: To play this game you will be given choices you will pick \n using numbers")
checkControls = input("Unknown: Do you under stand? \n 1: Yes\n 2: No\nYou: ")

if checkControls == "2":
    print("Unknown: You just used them...")
    time.sleep(3)
    print("Unknown: So you must understand...")
    time.sleep(3)
    checkLieCC = input("Were you lying? \n 1: Yes\n 2: No\nYou: ")
    if checkLieCC == "2":
        print("Unknown: YOU HAVE TO BE!!!")
        time.sleep(2)
        print("Unknown: Sorry I was over reacting")
        print("Unknown: I'm just going to asume you understand")
