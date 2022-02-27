from Player import Player


class Validator():

    @staticmethod
    def ask_if_should_keep_playing() -> bool:
        while True:
            choice = input('Quer jogar novamente? S / N\n').upper()
            if choice != 'S' and choice != 'N':
                print('Opção inválida.\n')
                continue
            return choice == 'S'

    @staticmethod
    def get_valid_position(player: Player) -> "list[int]":
        while True:
            position = input(
                f'Qual posição o {player.marker} quer marcar? (Linha Coluna) ').split()

            if len(position) != 2 or not Validator.is_position_valid(position):
                print('Entrada inválida, tente novamente.\n')
                continue
            break
        return [int(value) for value in position]

    @staticmethod
    def is_position_valid(position: "list[str]") -> bool:
        return position[0].isnumeric() and position[1].isnumeric() and 0 < int(position[0]) <= 3 and 0 < int(position[1]) <= 3
