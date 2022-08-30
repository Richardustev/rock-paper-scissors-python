#Rock, paper, scissors
import random
sys = False

def rps(player, selected):
    randomInt = random.randint(1, 3)
    randomIntSelected = ""
    if int(player) == int(randomInt):
        print("\n--Draw--\n")
    elif int(player) == 1 and int(randomInt) == 2:
        randomIntSelected = "Paper"
        print("\nYou loose!, You: {0} : Computer: {1}\n".format(selected, randomIntSelected))
    elif int(player) == 1 and int(randomInt) == 3:
        randomIntSelected = "scissors"
        print("\nYou Won!, You: {0} : Computer: {1}\n".format(selected, randomIntSelected))
    elif int(player) == 2 and int(randomInt) == 1:
        randomIntSelected = "Rock"
        print("\nYou Won!, You: {0} : Computer: {1}\n".format(selected, randomIntSelected))
    elif int(player) == 2 and int(randomInt) == 3:
        randomIntSelected = "Scissors"
        print("\nYou loose!, You: {0} : Computer: {1}\n".format(selected, randomIntSelected))
    elif int(player) == 3 and int(randomInt) == 2:
        randomIntSelected = "Paper"
        print("\nYou Won!, You: {0} : Computer: {1}\n".format(selected, randomIntSelected))
    elif int(player) == 3 and int(randomInt) == 1:
        randomIntSelected = "Rock"
        print("\nYou loose!, You: {0} : Computer: {1}\n".format(selected, randomIntSelected))
    else:
        sys == False
    
    sysRepeat = False

    while sysRepeat == False:
        repeat = input("Do you want to try another round? y/n:\n")

        if repeat == "y":
            sysRepeat == True
            print("")
            return sys == False
        elif repeat == "n":
            exit()
        else:
            print("Select a valid option...\n")
            sysRepeat == False
            break

while sys == False:
    player = input("1. Rock\n2. Paper\n3. Scissors\nSelect an option: ")
    selected = ""

    if player == "1":
        print("You have chosen rock.")
        selected = "Rock"
        rps(player, selected)
    elif player == "2":
        print("You have chosen paper.")
        selected = "Paper"
        rps(player, selected)
    elif player == "3":
        print("You have chosen scissors.")
        selected = "Scissors"
        rps(player, selected)
    else:
        print("Please, select a valid option.")
        sys = False