#!/usr/bin/env python
# pylint: disable=unused-argument

from telegram import Update
from telegram.ext import (
    ConversationHandler,
    ContextTypes,
    CallbackQueryHandler,
)

from bot.common.constants import STATE
from bot.common.utils import only


async def battle_ship_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "Морской бой. В разработке..."
    )

    await update.effective_user.send_message(text=text)
    return STATE.BATTLE_SHIP


battle_ship_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(battle_ship_menu, pattern=only(STATE.BATTLE_SHIP))],
    states={
        # EMPTY STATES
    },
    fallbacks=[]
)

