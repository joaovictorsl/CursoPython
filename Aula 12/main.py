# Criar um jogo da velha no terminal
# Loop se quiser jogar:
#     Fazer a grade do jogo
#     Esquema de turnos
#     Verificar se alguém ganhou
#     Guardar o placar
from tictactoe_functions import has_player_won, move, print_grid
import os

player1, player2 = 'X', 'O'


while True:
    winner = None
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print_grid(grid)
    for plays in range(1, 10):
        player = player1 if plays % 2 != 0 else player2
        move(player, grid)
        print('-'*50)
        print_grid(grid)
        if plays >= 5:
            if has_player_won(grid):
                winner = player
                break
    if winner:
        print(f'{winner} ganhou')
    else:
        print('Velha!')
    choice = input('Quer jogar novamente? S / N\n')
    # Validar o choice
    os.system('clear')
    if choice == 'S':
        player1, player2 = player2, player1
    else:
        break
