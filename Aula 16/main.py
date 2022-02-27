import os
from TicTacToe import TicTacToe
from Player import Player
from Validator import Validator

player1, player2 = Player('X'), Player('O')

game = TicTacToe(player1, player2)


while True:
    game.start()
    game.show_grid()

    for plays in range(1, 10):
        game.player_make_move(plays)
        print('-'*50)
        game.show_grid()

        if game.has_winner():
            break

    game.show_result()
    game.show_score()

    keep_playing = Validator.ask_if_should_keep_playing()

    os.system('clear')

    if keep_playing:
        game.invert_players()
    else:
        break
