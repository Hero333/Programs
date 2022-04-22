#! usr/bin/env python
# Format may look weird as it is programed in an online IDE
# Hours spent on program =~ 4 
checkPoint = 0

def stats(points):

    global strength
    global resistance
    global magic
    global agility
    global language 
    
    strength = 0
    resistance = 0
    magic = 0
    agility = 0
    language = 0
    
    # Few errors with this function
    end = True
    pointsUsed = 0
    pointsSpent = 0
    while end:
        print("Here are your stats: ")
        print("\n-------------------")
        print("Strength : " + str(strength) + "\nResistance : " + str(resistance) + "\n##### : " + str(magic) + "\nagility: " + str(agility) + "\nlanguage: " + 
        str(language)) 
        print("-------------------\n")
        pointsUseable = points - pointsSpent
        spend = input("What would you like to add a point to? Or use 6 to leave\n1: Strength\n2: Resistance \n3: #####\n4: agility\n5: language\n6: Leave\nYou: ")
        if spend == "1":
            if pointsUseable >= 1:
                strength = strength + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "2":
            if pointsUseable >= 1:
                resistance = resistance + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "3":
            if pointsUseable >= 1:
                magic = magic + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "4":
            if pointsUseable >= 1:
                agility = agility + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "5":
            if pointsUseable >= 1:
                language = language + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "6":
            break
            
stats(2)
while False:
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
