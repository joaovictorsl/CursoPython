def move(player: str, grid: "list[list[int | str]]"):
    row, column = [int(value) for value in input(
        f'Qual posição o {player} quer marcar? ').split()]
    # Verificar se a position é válida
    grid[row - 1][column - 1] = player


def print_grid(grid: "list[list[int | str]]"):
    for row in grid:
        for column in row:
            print(column, end=' ')
        print()


def has_player_won(grid: "list[list[int | str]]"):
    win_situations = [
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

    for situation in win_situations:
        values = []
        for row, column in situation:
            values.append(grid[row - 1][column - 1])
        if all(values):
            if values[0] == values[1] == values[2]:
                return True
    return False
