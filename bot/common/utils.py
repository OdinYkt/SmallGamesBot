import logging


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

