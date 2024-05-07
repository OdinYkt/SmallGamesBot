from bot.common.utils import Counter, split_to
from bot.common.dataclasses_ import Position

from .core import TicTacToeGame, SIZE


DATA_TO_FIELD_MAP = {Counter.give_one(): Position(x=x, y=y) for x in range(SIZE) for y in range(SIZE)}


class GameManager:
    # Паттерн наблюдатель
    def __init__(self):
        self.game = TicTacToeGame()




    @staticmethod
    def _get_data_to_field_map():
        return DATA_TO_FIELD_MAP


FIELD_KEYS = FIELD_CELLS.keys()
row1, row2, row3 = split_to([*FIELD_KEYS], chunk_count=3)
rows = (row1, row2, row3)


empty_field = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=EMPTY.EMPTY.value, callback_data=key) for key in row] for row in rows]
)