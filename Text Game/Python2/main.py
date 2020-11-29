# map

locations = [
    "Pat's",
    "Karla's",
    "Tata's",
    "Mom's",
    "Nona's",
]

location_benesses = { 
    "Pat's": [
        "Gabriel",
        "Bilbo",
        "Thorin",
        "Francisca",
    ],
    "Karla's": [
        "Nero",
        "Martin",
        "Naria",
        "Frederico",
    ],
    "Tata's": [
        "Miners", 
    ],
    "Mom's": [
        "Mika",
        "Chanel",
        "Guinness",
        "Mary",
    ],
    "Nona's": [
        "Frederico",
        "Francisco",
        "Preta"
    ],

}

location_descriptions = {
    "Pat's": "Gordinha's house.",
    "Karla's": "Mig's house.",
    "Tata's": "Nena's house.",
    "Mom's": "Mama's house.",
    "Nona's": "Granny's house."
}

# player's details and actions

class Player(object):

    def __init__(self):
        self.name = raw_input("Name, plz: ")
        self.location = "House"
        self.inventory = ["dress", "phone" , "lipstick", "cat1", "cat2", "cat3", "water bootle", "thermos"]
        self.health = 100
        self.gold = 100

    def menu(self):
        options = [
            "Go somewhere",
            "Inventory"
        ]
        action = pick_one(options)
        if action == "Go somewhere":
            self.travel()
        elif action == "Inventory":
            self.list_inventory()
        else: 
            raise StandardError ("Action (%s) is not in Player.menu()!" % str(action))

    def list_inventory(self):
        print "Your inventory:"
        for item in self.inventory:
            print " -",item
            print "%s gold coins! :D" % str (self.gold)


# main game loop

def main():
    player = Player()
    while True:
        assert player.location in locations
        "This isn't a valid location (%s)! I'm not sure how you got here..." % str (locations)
        print ""
        print location_descriptions
         [player.location])
            if player.location == "House":
                pass
            elif player.location == "Pat's":
                print "A wild cat appears"
                pet_cat = yes_or_no("Do you want to pet the cat?")

# CORRECT This
# answer = input("Enter yes or no: ") 
# if answer == "yes": 
#     # Do this. 
# elif answer == "no": 
#     # Do that. 
# else: 
#     print("Please enter yes or no.") 

            if pet_cat:
                player.gold = player.gold + 1
                print "the cat has given you a gold coin! You now have %x coins" % str(player.gold)
            else:
                print "You prefer to be a sad person and to not fluff the fluffy"
        elif player.location == "Karla's":
            if player.gold >= 10:
                buy_treats = yes_or_no("Do you wanna buy some treats?")
                    if buy_treats:
                        player.gold = player.gold - 10
                        player.inventory.append("yummy treats!")
                        print "you bought treats"
                    else: 
                        print "Fine, then"
            else:
                print "You need more din-din"
        else:
            raise StardatError ("There's no code for this location (%s) in main()!" % str(location)
        player.menu()


# other functions
