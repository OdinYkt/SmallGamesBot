from .constants import Move, SIZE


class WrongMoveException(Exception):
    def __init__(self, move: Move, reason: str):
        super(WrongMoveException, self).__init__()
        self.reason = reason
        self.move = move

    def __str__(self):
        return f"{self.reason} | x={self.move.x} y={self.move.y} | Player={self.move.player}"

    def __repr__(self):
        return str(self)


class CellMarkedException(WrongMoveException):
    def __init__(self, move: Move):
        super().__init__(move, reason="Cell is already marked!")


class OutOfFieldException(WrongMoveException):
    def __init__(self, move: Move):
        super().__init__(move, reason=f"Move coordinates out of field! Field size: {SIZE}")
