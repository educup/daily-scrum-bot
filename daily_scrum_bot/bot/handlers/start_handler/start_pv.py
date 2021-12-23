from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram.update import Update

from daily_scrum_bot.bot.handlers.start_handler.start_pv_texts import *


def start_pv_callback_handler(update: Update, context: CallbackContext):
    first_name = update.message.from_user.first_name
    update.message.reply_text(start_pv_hello(first_name))


start_pv_command_handler = CommandHandler(
    command=["start"],
    callback=start_pv_callback_handler,
)
