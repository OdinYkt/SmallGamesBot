from enum import Enum
from typing import Union, List
from dataclasses import dataclass

from bot.common.dataclasses_ import Position


class EMPTY(Enum):
    EMPTY = ' '


SIZE = 3


class Player(Enum):
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return str(self)


@dataclass
class Move:
    pos: Position
    player: Union[Player, EMPTY] = EMPTY.EMPTY

    def __str__(self) -> str:
        return f"'{self.player}'"

    def __repr__(self) -> str:
        return str(self)


class Direction(Enum):
    row = 0
    column = 1
    diagonal_left_right = 2
    diagonal_right_left = 3


@dataclass
class WinResult:
    winner: Player
    direction: Direction
    cells: List[Move]

    def have_winner(self) -> bool:
        return bool(self.winner)


@dataclass
class DrawResult:
    ...


GAME_RESULT = Union[WinResult, DrawResult]

EMPTY_FIELD = [[Move(pos=Position(x=row, y=column)) for column in range(SIZE)] for row in range(SIZE)]
