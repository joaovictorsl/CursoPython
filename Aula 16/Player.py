class Player():

    def __init__(self, marker) -> None:
        self.marker = marker
        self.__wins = 0

    def won(self):
        self.__wins += 1

    def get_wins(self):
        return self.__wins
