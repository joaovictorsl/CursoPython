from Player import Player
from Validator import Validator


class TicTacToe():

    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        self.__win_situations = [
            # Horizontais
            [[1, 1], [1, 2], [1, 3]],
            [[2, 1], [2, 2], [2, 3]],
            [[3, 1], [3, 2], [3, 3]],
            # Verticais
            [[1, 1], [2, 1], [3, 1]],
            [[1, 2], [2, 2], [3, 2]],
            [[1, 3], [2, 3], [3, 3]],
            # Diagonais
            [[1, 1], [2, 2], [3, 3]],
            [[1, 3], [2, 2], [3, 1]],
        ]

    def start(self):
        self.__winner = None
        self.__grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def player_make_move(self, plays: int):
        player = self.player1 if plays % 2 != 0 else self.player2
        self.move(player, plays)

    def move(self, player: Player, plays: int):
        is_possible_to_win = plays >= 5

        row, column = Validator.get_valid_position(player)

        self.__grid[row - 1][column - 1] = player.marker
        if is_possible_to_win:
            if self.__player_won(player):
                self.__winner = player.marker
                player.won()

    def __player_won(self, player: Player) -> bool:
        for situation in self.__win_situations:
            values = []
            for row, column in situation:
                value_from_grid = self.__grid[row - 1][column - 1]
                values.append(value_from_grid)

            if all(values):
                if values[0] == values[1] == values[2]:
                    return True
        return False

    def has_winner(self) -> str:
        return self.__winner

    def invert_players(self) -> None:
        self.player1, self.player2 = self.player2, self.player1

    def show_result(self) -> None:
        if self.__winner:
            print(f'{self.__winner} ganhou')
        else:
            print('Velha!')

    def show_score(self) -> None:
        print(f'{self.player1.marker} - {self.player1.get_wins()} | {self.player2.marker} - {self.player2.get_wins()}')

    def show_grid(self) -> None:
        for row in self.__grid:
            for value in row:
                print(value, end=' ')
            print()
