#! usr/bin/env python
# Format may look weird as it is programed in an online IDE
checkPoint = 0
strength = 0
resistance = 0
magic = 0
agility = 0
language = 0

def stats(points):
    # Many errors with this function
    end = True
    pointsUsed = 0
    while end:
        print("Here are your stats: ")
        print("\n-------------------")
        print("Strength : " + str(strength) + "\nResistance : " + str(resistance) + "\n 3: ##### : " + str(magic) + "\nagility: " + str(agility) + "\nlanguage: " + str(language)") 
        pointsUseable = points - pointsUsed 
        spend = input("What would you like to add a point to?\n1: Strength\n2: Resistance 3: #####")
while True:
    import time,random
    if checkPoint == 0:
        print("Hello and welcome to [insert text here]")
        print("Unknown: Hello, Player")
        print("Unknown: To play this game you will be given choices you will pick \n using numbers")
        checkControls = input("Unknown: Do you under stand? \n 1: Yes\n 2: No\nYou: ")
        
        if checkControls == "2":
            print("Unknown: You just used them...")
            time.sleep(2)
            print("Unknown: So you must understand...")
            time.sleep(2)
            checkLieCC = input("Were you lying? \n 1: Yes\n 2: No\nYou: ")
            if checkLieCC == "1":
                askLieCC = input("Unknown: Why would you do that?\n 1: I felt like it\n 2: To see if I could")
                if askLieCC == "2" or "1":
                    print("Unknown: Selfish whims")
                    print("Unknown: However we can begin...")
                    
            if checkLieCC == "2":
                print("Unknown: YOU HAVE TO BE!!!")
                time.sleep(2)
                print("Unknown: Sorry I was over reacting")
                print("Unknown: I'm just going to assume you understand")
                print("Let us begin...")
                
        if checkControls == "1":
            print("Unknown: Good.")
            print("Unknown: Then we can begin...")
            
        checkReady = input("Unknown: Are you ready? \n 1: Yes\n 2: Yes\n You: ")
        
        print("I suppose I should tell you what [insert text here] is")
        checkPoint = checkPoint + 1
        if checkPoint == 1:
            print("[insert text here] is a game")
            print("A game in which you will find all you could want")
            print("There are skills in this game")
            print("As well as stats")
            print("We use turn based combat")
            print("As it is civilized")
            stats(0)
            
            
            
            
            
        
