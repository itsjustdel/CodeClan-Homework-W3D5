class Player:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        #quickly turn string list in to integer for cleaner game logic
        self.choiceInt = ["rock", "paper","scissors"].index(choice) #python! :S