#!/usr/bin/env python
# pylint: disable=unused-argument

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ConversationHandler,
    ContextTypes,
    CallbackQueryHandler,
)

from bot.common.constants import STATE
from bot.common.utils import ONLY, Counter, change_from_answer

from .game import SINGLE, FRIEND, RANDOM, game_handler, empty_field

RULES, BACK = Counter(2)


async def tic_tac_toe_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Выберите с кем будете играть"
    )
    buttons = [
        [
            InlineKeyboardButton(text="Одиночная", callback_data=SINGLE),
            InlineKeyboardButton(text="С другом", callback_data=FRIEND)
        ],
        # InlineKeyboardButton(text="Случайный человек"),
        [
            InlineKeyboardButton(text="Правила", callback_data=RULES)
        ],
    ]
    markup = InlineKeyboardMarkup(buttons)

    await update.effective_user.send_message(text=text, reply_markup=markup)
    await change_from_answer(update, new_text="Крестики-Нолики")

    return STATE.TIK_TAC_TOE


async def single_play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Одиночная игра в крестики-нолики"
    )

    await update.effective_user.send_message(text=text, reply_markup=empty_field)
    await change_from_answer(update, new_text="Одиночная")

    return SINGLE


async def friend_play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Игра с друзьями. В разработке.."
    )

    await update.effective_user.send_message(text=text)
    await change_from_answer(update, new_text="Игра с друзьями")

    return STATE.TIK_TAC_TOE


async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Правила. В разработке.."
    )

    await update.effective_user.send_message(text=text)
    await change_from_answer(update)

    return STATE.TIK_TAC_TOE

tic_tac_toe_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(tic_tac_toe_menu, pattern=ONLY(STATE.TIK_TAC_TOE))],
    states={
        STATE.TIK_TAC_TOE: [
            CallbackQueryHandler(single_play,  pattern=ONLY(SINGLE)),
            CallbackQueryHandler(friend_play,  pattern=ONLY(FRIEND)),
            CallbackQueryHandler(rules,  pattern=ONLY(RULES)),
        ],
        SINGLE: [game_handler],
        # FRIEND: ...,
        # RULES: ...,

    },
    fallbacks=[]
)


