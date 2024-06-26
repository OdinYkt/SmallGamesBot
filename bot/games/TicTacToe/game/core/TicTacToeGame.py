from typing import Optional, List, NoReturn
from copy import deepcopy

from .constants import (
    EMPTY,
    SIZE,
    Player,
    WinResult,
    Direction,
    Move,
    DrawResult,
    GAME_RESULT,
    EMPTY_FIELD
)
from .exceptions import (
    CellMarkedException,
    OutOfFieldException,
)


class TicTacToeGame:
    def __init__(self):
        self.field = deepcopy(EMPTY_FIELD)
        self._directions = {
            Direction.row: self.row,
            Direction.column: self.column,
        }
        self._diagonals = {
            Direction.diagonal_left_right: self.diagonal_left_right,
            Direction.diagonal_right_left: self.diagonal_right_left,
        }

    def row(self, index: int) -> List[Move]:
        return self.field[index]

    def column(self, index: int) -> List[Move]:
        return [row[index] for row in self.field]

    def diagonal_left_right(self) -> List[Move]:
        return [row[i] for i, row in enumerate(self.field)]

    def diagonal_right_left(self) -> List[Move]:
        return [row[SIZE - 1 - i] for i, row in enumerate(self.field)]

    def make_move(self, move: Move) -> Optional[NoReturn]:
        if move.pos.x < 0 or move.pos.y < 0 or move.pos.x >= SIZE or move.pos.y >= SIZE:
            raise OutOfFieldException(move=move)

        if self.field[move.pos.x][move.pos.y].player != EMPTY.EMPTY:
            raise CellMarkedException(move=move)
        self.field[move.pos.x][move.pos.y] = move

    def get_result(self) -> Optional[GAME_RESULT]:
        """Return result of game or None"""
        win_result = self.winner
        if win_result:
            return win_result
        if not self.have_empty_cells():
            return DrawResult()
        return

    @property
    def winner(self) -> Optional[WinResult]:
        """Return winner player or None"""

        for direction, getter in self._directions.items():
            for index in range(SIZE):
                cells = getter(index)    # type:ignore
                result = WinResult(
                    winner=self._get_winner(cells),
                    direction=direction,
                    cells=cells
                )
                if result.have_winner():
                    return result

        for diagonal, getter in self._diagonals.items():
            cells = getter()
            result = WinResult(
                winner=self._get_winner(cells),
                direction=diagonal,
                cells=cells
            )
            if result.have_winner():
                return result

    def have_empty_cells(self) -> bool:
        for i in range(SIZE):
            if EMPTY.EMPTY in [cell.player for cell in self.row(i)]:
                return True
        return False

    @staticmethod
    def _get_winner(cells: List[Move]) -> Optional[Player]:
        winner = [*set([cell.player for cell in cells])]
        if len(winner) == 1 and winner[0] != EMPTY.EMPTY:
            return winner[0]

