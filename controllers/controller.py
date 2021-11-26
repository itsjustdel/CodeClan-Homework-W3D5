from flask import render_template, request
from app import app
from models.player import Player
from models.player_list import players
from models.game import *

@app.route('/game/')
def index():
    # going home, clear list of players, we will re-populate on next game
    players.clear()
    return render_template('index.html', title='Rock, Paper, Scissors!')

@app.route('/game/<choice1>/<choice2>/')
def play_game(choice1,choice2):
    
    player1 = Player("Agamemnon", choice1)
    player2 = Player("Achilles", choice2)
    player_list = [player1, player2]

    winning_player = winner(player1,player2)

    return render_template('outcome.html',player_list=player_list, winning_player=winning_player)

@app.route('/pvp/') #add var for button name?
def pvp():
    return render_template('pvp.html')

@app.route('/add_player', methods=['POST'])
def add_player():
    player = Player(request.form['name'], request.form['choice'])
    # add to our list we have declared in player_list.py    
    players.append(player)

    if(len(players) == 2):
        return render_template('outcome.html',player_list=players, winning_player=winner(players[0],players[1]))
    else:
        return pvp()