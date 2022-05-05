#! usr/bin/env python
# Format may look weird as it is programed in an online IDE
import random

checkPoint = 0
magicUnlock = "False"

strength = 3
resistance = 3
magic = 0
agility = 3
language = 1
hitPoints = 15

def mChoice():
    choice = random.randrange(1,3)
    if choice == 1:
        return "attack"
    if choice == 2:
        return "block"
    if choice == 3:
        return "dodge"

def combat(mName, mStrength, mResistance, mMagic, mAgility, mLanguage, mHitPoints):

    global strength
    global resistance
    global magic
    global agility
    global language
    global hitPoints

    print("Name: " + str(mName) + "\nStrength: " + str(mStrength) + "\nResistance: " + str(mResistance) + "\nMagic: " + str(mMagic) + "\nAgility: " + str(mAgility) + "\nLanguage: " + str(mLanguage))

    while hitPoints > 0:
            print(str(mName) + " has " + str(mHitPoints) + " remaining")
            print("You have " + str(hitPoints) + " remaining")
            playerCombatChoice = input("What would you like to do\n1: Attack\n2: Block\n3: Dodge\n4: Talk\nYou: ")
            if playerCombatChoice == "1":
                #if mChoice() == "attack":
                if (mStrength + random.randrange(1, 10)) > (strength + random.randrange(1, 10)):
                    hitPoints = hitPoints - (mStrength- resistance)
                    print("You took damage")

                else:
                    mHitPoints = mHitPoints - (strength - mResistance)
                    print(mName + " took damage")



def stats(points):

    global strength
    global resistance
    global magic
    global agility
    global language
    global hitPoints

    # Few errors with this function
    pointsSpent = 0
    while True:
        print("Here are your stats: ")
        print("\n-------------------")
        print("Strength : " + str(strength) + "\nResistance : " + str(resistance) + "\n##### : " + str(
            magic) + "\nAgility: " + str(agility) + "\nLanguage: " +
              str(language))
        print("\n-------------------\n")
        pointsUsable = points - pointsSpent
        print("You have " + str(pointsUsable) + " points")
        spend = input(
            "What would you like to add a point to? Or use 6 to leave\n1: Strength\n2: Resistance \n3: #####\n4: agility\n5: language\n6: Leave\nYou: ")
        if spend == "1":
            if pointsUsable >= 1:
                strength = strength + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "2":
            if pointsUsable >= 1:
                resistance = resistance + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "3":
            if magicUnlock == "True":
                if pointsUsable >= 1:
                    magic = magic + 1
                    pointsSpent = pointsSpent + 1
                else:
                    print("You do not have enough points for this")
                    break
            else:
                time.sleep(1)
                print("⠀")
                print("ERROR\n")

        if spend == "4":
            if pointsUsable >= 1:
                agility = agility + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "5":
            if pointsUsable >= 1:
                language = language + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points for this")
                break
        if spend == "6":
            break
stats(1)

combat("test", 5, 5, 0, 1, "english", 15)

while True:
    import time, random

    if checkPoint == 0:
        print("Hello and welcome to [Insert Text Here]")
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

        print("Unknown: I suppose I should tell you what [insert text here] is")
        checkPoint = checkPoint + 1
        if checkPoint == 1:
            print("Unknown: [insert text here] is a game")
            time.sleep(2)
            print("Unknown: A game in which you will find all you could want")
            time.sleep(2)
            print("Unknown: Where we use stats")
            time.sleep(1)
            print("Unknown: Here I'll show you your stats")
            time.sleep(2)
            print("Unknown: I'll even give you some points")
            stats(4)
            print("Unknown: If you didn't use some of those points")
            time.sleep(1)
            print("Unknown: They are gone forever")
            print("Unknown: See")
            stats(0)
            print("Unknown: So that would suck if you didn't spend some of those")
            time.sleep(2)
            print("Unknown: Now its time for combat!!")
            print("Unknown: In combat if you attack and your opponent does the same damage will be delt")
            print("Unknown: Your strength subtracted by the opponents strength")
            print("Unknown: If your opponent has higher strength you will take damage equal to their strength subtracted by your resistance")
            print("Unknown: If you attack and your opponent blocks damage will be delt your resistance - opponents strength")
            print("Unknown: This works the same if you block and your opponent attacks")
            print("Unknown: If you dodge and are successful no damage will be taken")
            print("Unknown: Dodging works with a random number combined with your agility against a random number against opponents agility")
            print("Unknown: If a dodge and a block both happen or a dodge and a dodge or a block and a block")
            print("Unknown: Nothing happens")
            print("Unknown: You could always try to talk to your opponent but you'll need to speak their language")
            print("Unknown: try it out!")
            combat("Bill the Pill", 3, 2, 0, 1, "english", 100)
