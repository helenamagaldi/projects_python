##### Simple Python Game Framework
##### To be modified into a text game of whatever flavor you want.

##### Information about the Map

locations = [
    "House",
    "Town Square",
    "Store",
]

location_connections = {
    "House": [
        "Town Square",
    ],
    "Store": [
        "Town Square",
    ],
    "Town Square": [
        "House",
        "Store",
    ],
    
}

location_descriptions = {
    "House": "This is your house.",
    "Town Square": "This is the center of the town.",
    "Store": "This is a store. They sell things here."
}



##### Information about the Player and the Player's Actions

class Player(object):

    ## This is run when we create a new player.
    ## Modify this if you want to store more information about the player.
    def __init__(self):
        self.name = raw_input("Enter your adventurer's name: ")
        self.location = "House"
        self.inventory = ["a red shirt", "pants"]
        self.health = 100
        self.gold = 0

    ## This is run at the end of every turn.
    ## Modify it if you want to add more actions.
    ## Then, create functions for those actions, below.
    def menu(self):
        options = [
            "Travel somewhere new",
            "Show your inventory"
        ]
        action = pick_one(options)
        if action == "Travel somewhere new":
            self.travel()
        elif action == "Show your inventory":
            self.list_inventory()
        else:
            ## If the code gets here, something went wrong!
            raise StandardError("There's no code for this action (%s) in Player.menu()!" % str(action))
            

    ## Travel to a new location.
    def travel(self):
        options = location_connections[self.location]
        options = sorted(list(set(options)))
        new_location = pick_one(options)
        self.location = new_location

    ## List the player's inventory.
    def list_inventory(self):
        print "Your inventory:"
        for item in self.inventory:
            print " -",item
        print "You have %s gold coins." % str(self.gold)



##### The Main Game Loop

def main():
    player = Player()
    while True:
        assert player.location in locations, "This isn't a valid location (%s)! I'm not sure how we got here..." % str(location)
        print ""
        print location_descriptions[player.location]
        if player.location == "House":
            pass
        elif player.location == "Town Square":
            print "There is a fountain here."
            loot_fountain = yes_or_no("Loot the fountain for money?")
            if loot_fountain:
                player.gold = player.gold + 1
                print "You find a coin! You now have %s coins." % str(player.gold)
            else:
                print "You prefer to remain dignified."
        elif player.location == "Store":
            if player.gold >= 10:
                buy_sword = yes_or_no("Buy a sword for 10 gold coins?")
                if buy_sword:
                    player.gold = player.gold - 10
                    player.inventory.append('a pretty cool sword')
                    print "You buy a sword."
                else:
                    print "Not today, then."
            else:
                print "You need 10 gold coins to buy a sword. Come back later."
        else:
            ## If the code gets here, something went wrong!
            raise StandardError("There's no code for this location (%s) in main()!" % str(location))
        player.menu()



###### Helpful Functions

def yes_or_no(question):
    print ""
    assert type(question) is str, "You need to call yes_or_no with a string."
    while True:
        user_input = raw_input(question + " (y/n) ")
        if len(user_input) > 0:
            first_char = user_input[0]
            if first_char.lower() in ["y", "t"]:
                return True
            elif first_char.lower() in ["n", "f"]:
                return False
            else:
                print "    Please enter y or n."
        else:
            print "    Please enter y or n."

def pick_one(options):
    print ""
    assert type(options) is list, "You need to call pick_one with a list of strings."
    assert len(options) > 0, "You need to call pick_one with a non-empty list of strings."
    assert all([type(i) is str for i in options]), "You need to call pick_one with a list of strings."
    question = "Pick one:"
    for i in range(len(options)):
        question += "\n    (%s) %s" % (str(i+1), options[i])
    print question
    while True:
        user_input = raw_input("    Your choice = ")
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(options):
                return options[choice-1]
            else:
                print "    Please enter a number from 1 to %s." % str(len(options))
        else:
            print "    Please enter a number from 1 to %s." % str(len(options))



###### Running the Game

def consistency_check():
    ## You can delete this function if you want. All it does is check
    ## that you haven't forgotten anything.
    for location in locations:
        assert type(location) is str, "One of your locations (%s) isn't a string!" % str(location)
        assert location in location_connections, "One of your locations (%s) isn't listed in location_connections!" % location
        assert location in location_descriptions, "One of your locations (%s) isn't listed in location_descriptions!" % location
    for location, connections in location_connections.iteritems():
        assert type(location) is str, "One of your location_connections keys (%s) isn't a string!" % str(location)
        assert location in locations, "One of your location_connections keys (%s) isn't listed in locations!" % location
        assert type(connections) is list, "One of your location_connection values (%s) isn't a list!" % str(connections)
        for connection in connections:
            assert type(connection) is str, "One of your location_connection values (%s) contains a non-string!" % str(connections)
    for location, description in location_descriptions.iteritems():
        assert type(location) is str, "One of your location_descriptions keys (%s) isn't a string!" % str(location)
        assert location in locations, "One of your location_descriptions keys (%s) isn't listed in locations!" % location
        assert type(description) is str, "One of your location_description values (%s) isn't a string!" % str(description)    

if __name__ == '__main__':
    consistency_check()
    main()


    
