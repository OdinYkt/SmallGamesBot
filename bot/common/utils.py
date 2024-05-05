import logging
from typing import Iterator, Optional, List
from copy import deepcopy

from telegram import Update


def ONLY(something: str) -> str:
    return "^" + str(something) + "$"


def ANY(something: List[str]) -> str:
    return "^(?:" + '|'.join(something) + ')$'


def setup_logger() -> None:
    """
    Setup logging
    From python-telegram-bot.examples
    """
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    # set higher logging level for httpx to avoid all GET and POST requests being logged
    logging.getLogger("httpx").setLevel(logging.WARNING)

    logging.getLogger('SmallGamesBot')


class _Counter:
    MAX_COUNT = 1000
    __counter = range(MAX_COUNT).__iter__()

    def __call__(self, count=1) -> Iterator[str]:
        return map(chr, (_Counter.__counter.__next__() for _ in range(count)))

    def give_one(self) -> str:
        return [*self()][0]


Counter = _Counter()


async def change_from_answer(update: Update, new_text: Optional[str] = None, text_holder: str = '◾ '):
    await update.callback_query.answer()
    if new_text:
        await update.callback_query.edit_message_text(text=text_holder+new_text, reply_markup=None)
    else:
        await update.callback_query.delete_message()


def split_to(original: List, chunk_count: int) -> List[List]:
    # добавить описание, возможно переделать
    # обрубает конец списка, если не влезает
    result = []
    _original = deepcopy(original)
    chunk_size = len(_original) // chunk_count
    for i in range(chunk_count):
        result.append(_original[chunk_size*i: chunk_size*(i + 1)])

    return result
