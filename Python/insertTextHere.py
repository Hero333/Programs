#! usr/bin/env python
# Format may look weird as it is programed in an online IDE

checkPoint = 0
magicUnlock = "False"

strength = 0
resistance = 0
magic = 0
agility = 0
language = 0
hitPoints = 100

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
            #Combat will not assign damage
            if playerCombatChoice == 1:
                #if mChoice() == "attack":
                if mStrength > strength:
                    hitPoints = hitPoints - (mStrength- resistance)

                if mStrength < strength:
                    mHitPoints = mHitPoints - (strength - mResistance)



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
        # I'm assuming that this is not Unknown talking,
        # So I'm adding the name System to this.
        print("System: ")
        print("Here are your stats: ")
        print("\n-------------------")
        print("Strength : " + str(strength) + "\nResistance : " + str(resistance) + "\n#####: " + str(
            magic) + "\nagility: " + str(agility) + "\nlanguage: " +
              str(language))
        print("\n-------------------")
        pointsUsable = points - pointsSpent
        print("You have " + str(pointsUsable) + " points.")
        spend = input(
            "What would you like to add a point to?\n1: Strength\n2: Resistance \n3: #####\n4: agility\n5: language\n6: Leave\nYou: ")
        # Im not going to do it here, (yet) but i recommend that you turn this from checking for a string to checking for a number
        if spend == "1":
            if pointsUsable >= 1:
                strength = strength + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points!")
                break
        if spend == "2":
            if pointsUsable >= 1:
                resistance = resistance + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points!")
                break
        if spend == "3":
            if magicUnlock == "True":
                if pointsUsable >= 1:
                    magic = magic + 1
                    pointsSpent = pointsSpent + 1
                else:
                    print("You do not have enough points!")
                    break
            else:
                time.sleep(1)
                print("⠀")
                print("System Error!\n")

        if spend == "4":
            if pointsUsable >= 1:
                agility = agility + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points!")
                break
        if spend == "5":
            if pointsUsable >= 1:
                language = language + 1
                pointsSpent = pointsSpent + 1
            else:
                print("You do not have enough points!")
                break
        if spend == "6":
            break
stats(1)

combat("test", 5, 5, 0, 1, "english", 100)

while True:
    import time, random

    if checkPoint == 0:
        print("Welcome to [insert text here]!")
        print("Unknown: Hello, Player.")
        print("Unknown: To play this game you will be given choices you will pick using numbers.")
        checkControls = input("Unknown: Do you understand? \n 1: Yes\n 2: No\nYou: ")

        if checkControls == "2":
            print("Unknown: You just used them...")
            time.sleep(2)
            print("Unknown: So you must understand...")
            time.sleep(2)
            checkLieCC = input("Were you lying? \n 1: Yes\n 2: No\nYou: ")
            if checkLieCC == "1":
                askLieCC = input("Unknown: Why would you do that?\n 1: I felt like it\n 2: To see if I could \nYou: ")
                if askLieCC == "2" or "1":
                    print("Unknown: Selfish whims!")
                    print("Unknown: However we can begin...")

            if checkLieCC == "2":
                print("Unknown: YOU HAVE TO BE!!!")
                time.sleep(2)
                print("Unknown: Sorry I was over-reacting.")
                print("Unknown: I'm just going to assume you understand.")
                print("Unknown: Let us begin...")

        if checkControls == "1":
            print("Unknown: Good.")
            print("Unknown: Then we can begin...")

        checkReady = input("Unknown: Are you ready?\n 1: Yes\n 2: Yes\nYou: ")

        print("Unknown: ")
        print("I suppose I should tell you what [insert text here] is.")
        checkPoint = checkPoint + 1
        if checkPoint == 1:
            print("[insert text here] is a game!")
            time.sleep(2)
            print("A game in which you will find everything you have ever wanted.")
            time.sleep(2)
            print("It even has a stats system!")
            time.sleep(1)
            print("I'll even give you some points for it.")
            stats(4)
            print("If you don't spend any of the points,")
            time.sleep(1)
            print("They are gone forever!")
            time.sleep(2)
            print("Spend them now, or regret it forever!")
            stats(0)
            print("Well, hopefully you spent them.")
            time.sleep(2)
            print("Now its time for combat!")
            print("In combat if you attack, and your opponent attacks too, damage will be dealt!")
            print("The damage dealt is your strength substracted by your opponents strength.")
            print("If your opponent has higher strength, the damage you take will be equal to their strength minus your resistance.")
            print("If you opponent blocks your attack, damage will be delt. It will be your resistance minus the oppoents strength.")
            print("This works the same if you block and your opponent attacks.")
            print("If you dodge and are successful no damage will be taken.")
            print("Dodging works with a random number combined with your agility against a random number against opponents agility.")
            print("If a dodge and a block both happen or a dodge and a dodge or a block and a block.")
            print("Nothing happens!")
            print("You could always try to talk to your opponent but you'll need to speak their language.")
            print("Try it out!")
            combat("Bill the Pill", 3, 2, 0, 1, "english", 100)
