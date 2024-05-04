from enum import Enum
from typing import Union, Optional
from dataclasses import dataclass


EMPTY = '_'
SIZE = 3
DRAW = 'DRAW'   #?


class Player(Enum):
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'

    def __repr__(self):
        return f"'{self.value}'"


class Direction(Enum):
    row = 0
    column = 1
    diagonal_left_right = 2
    diagonal_right_left = 3


@dataclass
class Move:
    x: int
    y: int


@dataclass
class WinResult:
    winner: Player
    direction: Direction
    index: Optional[int] = None

    def have_winner(self) -> bool:
        return bool(self.winner)


class Types:
    CELL = Union[Player, EMPTY]


class WrongMoveException(Exception):
    def __init__(self, player: Player, move: Move, reason: str):
        self.reason = reason
        self.player = player
        self.move = move

    def __str__(self):
        return f"Wrong move! {self.reason} | {self.player} | {self.move}"

    def __repr__(self):
        return str(self)
