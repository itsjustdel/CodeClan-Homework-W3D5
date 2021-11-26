from flask import render_template, request
from app import app
from models.player import Player
from models.player_list import players
from models.game import create_cpu_player, winner

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

@app.route('/add_player/<game_type>') #add var for button name?
def add_player_page(game_type):
    # button should read "Play!" if we already have a player in the list, or game is against cpu
    # ternary declaration
    button_text = "Play!" if len(players) == 1 or game_type == "pve" else "Next"
    # return page with two arguments
    return render_template('add_player_form.html',game_type=game_type,button_text=button_text)

@app.route('/add_player/<game_type>', methods=['POST'])
def add_player(game_type):
    player = Player(request.form['name'], request.form['choice'])
    # add to our list declared in player_list.py    
    players.append(player)
    
    # if player is playing against computer, add a computer
    if game_type == "pve":
        players.append(create_cpu_player())

    # check if we have enough players to play game (including computer)
    if len(players) == 2:
        return render_template('outcome.html',player_list=players, winning_player=winner(players[0],players[1]))
    else:
        # if we do not have enough, go to the page where we can add another player
        # carry the game type with us
        return add_player_page(game_type)