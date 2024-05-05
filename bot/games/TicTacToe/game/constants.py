from dataclasses import dataclass

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .core import EMPTY, SIZE
from bot.common.utils import Counter, split_to


SINGLE, RANDOM, FRIEND = Counter(3)


@dataclass
class Position:
    x: int
    y: int


FIELD_CELLS = {Counter.give_one(): Position(x=x, y=y) for x in range(SIZE) for y in range(SIZE)}

FIELD_KEYS = FIELD_CELLS.keys()
row1, row2, row3 = split_to([*FIELD_KEYS], chunk_count=3)
rows = (row1, row2, row3)


empty_field = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=EMPTY.EMPTY.value, callback_data=key) for key in row] for row in rows]
)
