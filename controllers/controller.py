from flask import render_template, request
from app import app
from models.player import Player, name_check
from models.player_list import players
from models.game import create_cpu_player, winner

@app.route('/game/')
def index():
    # going home, clear list of players, we will re-populate on next game
    players.clear()
    return render_template('welcome.html')

# test function to check if manually entering "rock", "paper", or "scissors" works        
@app.route('/game/<choice1>/<choice2>/')
def play_game(choice1,choice2):    
    player1 = Player("Agamemnon", choice1)
    player2 = Player("Achilles", choice2)
    _player_list = [player1, player2]

    winning_player = winner(_player_list)
    return render_template('outcome.html',player_list=_player_list, winning_player=winning_player)

@app.route('/add_player/<game_type>')
def add_player_next(game_type): 
    print("add player next")
    # ternary declaration to change text on submit button
    button_text = "Play!" if len(players) == 1 or game_type == "pve" else "Next"
    # return page with two arguments
    return render_template('add_player_form.html', game_type=game_type, button_text=button_text)

@app.route('/add_player/<game_type>', methods=['POST'])
def add_player(game_type):
    print("add player post")
    #create player instance from form data

    #check for empty name
    name = name_check(request.form['name'],players)

    player = Player(name, request.form['choice'])
    # add to our player list declared in player_list.py    
    players.append(player)
    
    # if player is playing against computer, add a computer
    if game_type == "pve":
        players.append(create_cpu_player())

    # check if we have enough players to play game (including computer)
    if len(players) == 2:
        return render_template('outcome.html',player_list=players, winning_player=winner(players)) 
    else:
        # if we do not have enough players yet, add another
        return add_player_next(game_type)
