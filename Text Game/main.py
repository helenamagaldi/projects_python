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
        self.name = input("Enter you name: ")
        self.location = "House"
        self.inventory = ["dress", "phone" , "lipstick", "cat1", "cat2", "cat3", "water bootle", "thermos"]
        self.health = 100
        self.gold = 100

    def menu(self):
        options = [
            "Go somewhere new",
            "Show your inventory"
        ]
        action = pick_one(options)
        if action == "Go somewhere new":
            self.travel()
        elif action == "Show your inventory":
            self.list_inventory()
        else: 
            raise StandardError ("There's no code for this action (%s) in Player.menu()!" % str(action))

    def list_inventory(self):
        print ("Your inventory:")
        for item in self.inventory:
            print (" -"),item
            print ("You have %s gold coins") % str (self.gold)


# main game loop

def main():
    player = Player()
    while True:
        assert player.location in locations
        "This isn't a valid location (%s)! I'm not sure how you got here..." % str (locations)
        print ("")
        print (location_descriptions
         [player.location])
        if player.location == "House":
             pass
        elif player.location == "Pat's"
