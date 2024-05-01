import logging
from typing import Iterator


def ONLY(something) -> str:
    return "^" + str(something) + "$"


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


Counter = _Counter()
