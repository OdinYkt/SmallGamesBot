from enum import Enum

EMPTY = '_'
SIZE = 3


class Player(Enum):
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'
    DRAW = 2

    def __repr__(self):
        return f"'{self.value}'"
