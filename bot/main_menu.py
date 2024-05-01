#!/usr/bin/env python
# pylint: disable=unused-argument

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from bot.games.TheBattleShip import battle_ship_handler
from bot.games.TicTacToe import tic_tac_toe_handler

from bot.common.constants import STATE, CONTEXT


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Привет!\n"
        "Выбери в какую игру ты хочешь играть\n"
        "В любой момент можешь остановить работу командой /stop\n"
    )
    buttons = [
        [
            InlineKeyboardButton(text="Крестики-Нолики", callback_data=STATE.TIK_TAC_TOE),
        ],
        [
            InlineKeyboardButton(text="Морской бой", callback_data=STATE.BATTLE_SHIP)
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(CONTEXT.START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        await update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[CONTEXT.START_OVER] = False
    return STATE.SELECTING_GAMES


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Текущее состояние прервано.\n"
        "Используйте /start чтобы начать с начала"
    )
    await update.message.reply_text(text=text)
    return STATE.END


async def not_recognized(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Сообщение не распознано\n"
        "Воспользуйтесь /stop, если хотите покинуть этот режим"
    )
    await update.message.reply_text(text=text)


main_menu_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        STATE.SELECTING_GAMES: [
            tic_tac_toe_handler,
            battle_ship_handler,
        ],
    },
    fallbacks=[
        CommandHandler("stop", stop),
        MessageHandler(filters.TEXT & ~filters.COMMAND, not_recognized)
    ],
)
