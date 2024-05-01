from dotenv import load_dotenv
load_dotenv()

from telegram import Update
from telegram.ext import Application

from bot.main_menu import main_menu_handler
from common.constants import BOT_TOKEN


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(main_menu_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

