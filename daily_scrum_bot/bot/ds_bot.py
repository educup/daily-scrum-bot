import logging

from telegram.ext import Updater, PicklePersistence

from daily_scrum_bot.bot.handlers import bot_handlers


class DailyScrumBot:
    def __init__(
        self,
        token: str,
    ) -> None:
        self.token = token
        self.logger = logging.getLogger(__name__)

        persistence = PicklePersistence(
            "ds_bot.data",
        )

        self.updater = Updater(
            token=token,
            persistence=persistence,
            arbitrary_callback_data=True,
        )

        dispatcher = self.updater.dispatcher

        for handler in bot_handlers:
            dispatcher.add_handler(handler)

    def log(
        self,
        message: object,
        level=logging.INFO,
    ):
        self.logger.log(
            level=level,
            msg=message,
        )

    def run(self):
        try:
            self.updater.start_polling()
        except Exception as e:
            self.log(str(e), level=logging.ERROR)
