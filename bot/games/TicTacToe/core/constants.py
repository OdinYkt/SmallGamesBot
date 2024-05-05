from enum import Enum
from typing import Union, Optional, List
from dataclasses import dataclass


EMPTY: str = '_'
SIZE = 3


class Player(Enum):
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return str(self)


CELL = Union[Player, EMPTY]


@dataclass
class Move:
    x: int
    y: int
    player: CELL = EMPTY

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