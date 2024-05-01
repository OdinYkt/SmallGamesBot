from typing import Optional
from dataclasses import dataclass

from bot.games.TicTacToe.core.constants import EMPTY, SIZE, Player


@dataclass
class Move:
    x: int
    y: int


class TicTacToeGame:
    def __init__(self):
        self.field = [[EMPTY]*SIZE for i in range(SIZE)]

    def make_move(self, player: Player, move: Move):
        if self.field[move.x][move.y] != EMPTY:
            # WRONG MOVE
            return
        self.field[move.x][move.y] = player

    def print_field(self):
        print(*self.field, sep='\n')
        print('\n')

    def _get_row_winner(self, row: int) -> Optional[Player]:
        winner = set(self.field[row])
        if len(winner) > 1:
            return None
        return list(winner)[0]

    def _get_column_winner(self, column: int):
        ...


    @property
    def winner(self) -> Optional[Player]:
        """Return winner player or None or draw"""


        return None


if __name__ == '__main__':
    game = TicTacToeGame()
    game.print_field()
    game.make_move(
        player=Player.PLAYER_1,
        move=Move(
            x=0,
            y=0,
        )
    )
    game.print_field()
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
            x=0,
            y=2,
        )
    )
    game._get_row_winner(0)