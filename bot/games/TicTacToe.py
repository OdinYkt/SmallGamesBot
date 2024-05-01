#!/usr/bin/env python
# pylint: disable=unused-argument

from telegram import Update
from telegram.ext import (
    ConversationHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from bot.common.constants import STATE
from bot.common.utils import only


async def tic_tac_toe_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Крестики нолики. В разработке..."
    )

    await update.effective_user.send_message(text=text)
    return STATE.TIK_TAC_TOE


tic_tac_toe_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(tic_tac_toe_menu, pattern=only(STATE.TIK_TAC_TOE))],
    states={
        # EMPTY STATES
    },
    fallbacks=[]
)


