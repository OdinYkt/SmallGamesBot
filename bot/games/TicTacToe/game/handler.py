#!/usr/bin/env python
# pylint: disable=unused-argument

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ConversationHandler,
    ContextTypes,
    CallbackQueryHandler,
)

from bot.common.utils import ONLY, ANY, Counter, change_from_answer

from .manager.constants import SINGLE, FIELD_CELLS, GAME, FIELD_KEYS, GAME_MANAGER
from .manager.GameManager import GameManager
from .manager.ManagerFactory import ManagerFactory


async def start_single_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.callback_query.answer()

    context.user_data[GAME_MANAGER] = ManagerFactory.get_manager_single_game(
        user=update.effective_user
    )
    return GAME


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    manager: GameManager = context.user_data[GAME_MANAGER]
    await manager.manage_player(user=update.effective_user, action=update.callback_query.data)
    return manager.get_user_state(player=update.effective_user)


game_handler = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(start_single_game, pattern=ANY(SINGLE))
    ],
    states={
        GAME: [CallbackQueryHandler(game, pattern=ANY(FIELD_KEYS))]
    },
    fallbacks=[]
)


