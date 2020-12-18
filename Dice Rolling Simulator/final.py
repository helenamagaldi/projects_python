import random

x = "y"

def start():
    print("Press x to roll the dice")

    answer = input(">").lower() 
    # just in the case the answer is uppercase

    if answer == "x":
        rolling_dice()
    else:
        print("Press x and x only")
        start()


# number = random.randint(1,6)

def rolling_dice():

    number = random.randint(1,6)

    if number == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("|       |")
        print("|   2   |")
        print("|       |")
        print("---------")
    elif number == 3:
        print("---------")
        print("|       |")
        print("|   3   |")
        print("|       |")
        print("---------")
    elif number == 4:
        print("---------")
        print("|       |")
        print("|   4   |")
        print("|       |")
        print("---------")
    elif number == 5:
        print("---------")
        print("|       |")
        print("|   5   |")
        print("|       |")
        print("---------")
    else:
        print("---------")
        print("|       |")
        print("|   6   |")
        print("|       |")
        print("---------")

    x = input("y or n")
    if x == "y":
        start()
    else:
        print("Game over")

start()