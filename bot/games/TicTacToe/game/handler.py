#!/usr/bin/env python
# pylint: disable=unused-argument

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ConversationHandler,
    ContextTypes,
    CallbackQueryHandler,
)

from bot.common.utils import ONLY, ANY, Counter, change_from_answer

from .constants import SINGLE, FIELD_CELLS, FIELD_KEYS


async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.callback_query.answer()
    print(FIELD_CELLS[update.callback_query.data])


async def single_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    print(FIELD_CELLS[update.callback_query.data])


game_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(start_game, pattern=ANY(FIELD_KEYS))],
    states={
        SINGLE: [CallbackQueryHandler(single_game, pattern=ANY(FIELD_KEYS))]
    },
    fallbacks=[]
)


