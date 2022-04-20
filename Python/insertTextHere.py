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
    if checkLieCC == "1":
        askLieCC = input("Unknown: Why would you do that?\n 1: I felt like it\n 2: To see if I could\n 3: Your face is ugly\nYou: ")
        if askLieCC == "1" or "2":
            print("Unknown: Selfish whims")
            checkReady = input("Unknown: Anyway are you ready? \n 1: Yes\n 2: Yes\n You: )
        if askLieCC == "3":
            print("You prick...")
            print("We are starting now...")
    if checkLieCC == "2":
        print("Unknown: YOU HAVE TO BE!!!")
        time.sleep(2)
        print("Unknown: Sorry I was over reacting")
        print("Unknown: I'm just going to assume you understand")
        
print("Unknown: Good.")
time.sleep(1)
print("Unknown: Then we can begin...")
