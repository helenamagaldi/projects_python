def start():
    print("You are in a room")
    print("There are two doors: one to your left and one to your right. Which one do you choose? (l or r)")

    answer = input(">").lower() 
    # just in the case the answer is uppercase

    if "l" in answer:
        bear_room()
    elif "r" in answer:
        monster_room()
    else:
        game_over("Sorry, that door does not exist")


def bear_room():
    print("BEAR")
    print("There's a door behind the bear")
    print("The bear wants to kill you")
    print("What would you do? (1 or 2")
    print("1). Punch the bear")
    print("2). Try to reason with the bear")

    answer = input(">")

    if answer == "1":
        game_over("Ok, you're dead. Never take food from a bear")
    elif answer == "2":
        print("The bear can't listen to your voice. It moved and you now can go through the door")
        diamond_room()
    else:
        game_over("I said 1 or 2")

def monster_room():
    print("A wild Bolsonaro appears")
    print("The Bolsonaro monster is sleeping. \nBehind it, there is another door")
    print("1). Go through the door silently")
    print("2). Kill it with fire")

    answer = input(">")

    if answer == "1":
        diamond_room()
    elif answer == "2":
        game_over("Fire can't kill a Bolsonaro. You're dead.")


def diamond_room():
    print("\nYou are in a room filled with diamonds")
    print("But here is another door")
    print("What will you do? (1 or 2")
    print("1). Take some rights and go through the door")
    print("2). Go through the door")

    answer = input(">")

    if answer == "1":
        game_over("Sorry, this money isn't yours. You're dead.")
    elif answer == "2":
        print("Honesty pays back. You won!")
        play_again()
    else: 
        game_over("Again, only 1 or 2. You're dead")

def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()

def play_again():
    print("\n Wanna play again? (y or n)")

    answer = input(">").lower()
    # 

    if "y" in answer:
        start()
    else:
        exit()

# start game 
start()