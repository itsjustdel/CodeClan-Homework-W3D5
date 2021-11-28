class Player:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        #quickly turn string list in to integer for cleaner game logic
        self.choiceInt = ["rock", "paper","scissors"].index(choice) #python!

def name_check(name_from_form, players):
    #check for empty name    
    name = name_from_form
    if name == "":
        name = "Player " + str(len(players)+1)
    
    return name