from typing import List
from telegram.ext.handler import Handler
from daily_scrum_bot.bot.handlers.start_handler import start_pv_command_handler


bot_handlers: List[Handler] = [
    start_pv_command_handler,
]
