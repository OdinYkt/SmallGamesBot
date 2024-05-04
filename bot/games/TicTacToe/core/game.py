from typing import Optional, List

from bot.games.TicTacToe.core.constants import (
    EMPTY,
    SIZE,
    Player,
    Types,
    WinResult,
    Direction,
    Move,
    WrongMoveException
)


class TicTacToeGame:
    def __init__(self):
        self.field = [[EMPTY]*SIZE for i in range(SIZE)]
        self._directions = {
            Direction.row: self.row,
            Direction.column: self.column,
        }
        self._diagonals = {
            Direction.diagonal_left_right: self.diagonal_left_right,
            Direction.diagonal_right_left: self.diagonal_right_left,
        }

    def row(self, index: int) -> List[Types.CELL]:
        return self.field[index]

    def column(self, index: int) -> List[Types.CELL]:
        return [row[index] for row in self.field]

    # TODO
    #   to one method?
    def diagonal_left_right(self) -> List[Types.CELL]:
        return [row[i] for i, row in enumerate(self.field)]

    def diagonal_right_left(self) -> List[Types.CELL]:
        return [row[SIZE - 1 - i] for i, row in enumerate(self.field)]
    ###

    def make_move(self, player: Player, move: Move) -> None:
        if move.x < 0 or move.y < 0 or move.x >= SIZE or move.y >= SIZE:
            raise WrongMoveException(player=player, move=move,
                                     reason=f"Move coordinates out of field! Field size: {SIZE}")

        if self.field[move.x][move.y] != EMPTY:
            raise WrongMoveException(player=player, move=move,
                                     reason="Cell is already marked!")
        self.field[move.x][move.y] = player

    @property
    def winner(self) -> Optional[WinResult]:
        """Return winner player or None or draw"""

        for direction, getter in self._directions.items():
            for index in range(SIZE):
                result = WinResult(
                    winner=self._get_winner(getter(index)),     # type:ignore
                    direction=direction,
                    index=index)
                if result.have_winner():
                    return result

        for diagonal, getter in self._diagonals.items():
            result = WinResult(
                winner=self._get_winner(getter()),
                direction=diagonal
            )
            if result.have_winner():
                return result

    def have_empty_cells(self) -> bool:
        for i in range(SIZE):
            for cell in self.row(i):
                if cell == EMPTY:
                    return True
        return False

    @staticmethod
    def _get_winner(cells: List[Types.CELL]) -> Optional[Types.CELL]:
        winner = [*set(cells)]
        if len(winner) == 1 and winner[0] != EMPTY:
            return winner[0]


if __name__ == '__main__':
    game = TicTacToeGame()
    game.make_move(
        player=Player.PLAYER_1,
        move=Move(
            x=0,
            y=0,
        )
    )
    game.make_move(
        player=Player.PLAYER_1,
        move=Move(
            x=0,
            y=1,
        )
    )
    game.make_move(
        player=Player.PLAYER_1,
        move=Move(
            x=1,
            y=0,
        )
    )
    game.make_move(
        player=Player.PLAYER_1,
        move=Move(
            x=2,
            y=0,
        )
    )
    print(game.winner)
