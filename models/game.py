def winner(player1, player2):
    # decision array idea from
    #https://codereview.stackexchange.com/questions/144013/rock-paper-scissors-c-game
    # Maps out all outcomes and selected by array index 
    # index 0 = rock, 1 = paper, 2 = scissors    
    # None = draw  
    decision_array = [[None,player2,player1],
                      [player1,None,player2],
                      [player2,player1,None]]
    

    return decision_array[player1.choiceInt][player2.choiceInt]