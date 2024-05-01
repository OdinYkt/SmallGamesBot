import os
from telegram.ext import ConversationHandler


BOT_TOKEN = os.getenv('BOT_TOKEN')


# TODO
#   Автоматически присваивать значения
#   Избавиться от range(хардкод)
# STATES
class State:
    END = ConversationHandler.END
    BATTLE_SHIP, TIK_TAC_TOE = map(chr, range(2))
    SELECTING_GAMES, = map(chr, range(2, 3))


# CONTEXT
class Context:
    START_OVER, = map(chr, range(100, 101))


STATE = State()
CONTEXT = Context()
