from .constants import Player, Move, SIZE


class WrongMoveException(Exception):
    def __init__(self, player: Player, move: Move, reason: str):
        self.reason = reason
        self.player = player
        self.move = move

    def __str__(self):
        return f"{self.reason} | {self.player} | {self.move}"

    def __repr__(self):
        return str(self)


class CellMarkedException(WrongMoveException):
    def __init__(self, player: Player, move: Move):
        super().__init__(player, move, reason="Cell is already marked!")


class OutOfFieldException(WrongMoveException):
    def __init__(self, player: Player, move: Move):
        super().__init__(player, move, reason=f"Move coordinates out of field! Field size: {SIZE}")
