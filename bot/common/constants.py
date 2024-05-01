import os
from telegram.ext import ConversationHandler

from bot.common.utils import Counter

BOT_TOKEN = os.getenv('BOT_TOKEN')


# STATES
class State:
    END = ConversationHandler.END
    BATTLE_SHIP, TIK_TAC_TOE = Counter(2)
    SELECTING_GAMES, = Counter()


# CONTEXT
class Context:
    START_OVER, = Counter()


STATE = State()
CONTEXT = Context()
