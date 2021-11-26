import random
from models.player import Player
def winner(players):
    # decision array idea from
    #https://codereview.stackexchange.com/questions/144013/rock-paper-scissors-c-game
    # Maps out all outcomes and selected by array index 
    # index 0 = rock, 1 = paper, 2 = scissors    
    # None = draw  
    decision_array = [[None,players[1],players[0]],
                      [players[0],None,players[1]],
                      [players[1],players[0],None]]
    

    return decision_array[players[0].choiceInt][players[1].choiceInt]

def create_cpu_player():
    return Player("Computer",choice_for_cpu())

def choice_for_cpu():
    return random.choice(["rock", "paper", "scissors"])