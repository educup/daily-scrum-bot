import logging
import typer
from daily_scrum_bot.bot import DailyScrumBot

from daily_scrum_bot.commands import user_app
from daily_scrum_bot.data import init
from daily_scrum_bot.settings import get_settings

settings = get_settings()
TOKEN = settings.telegram_bot_token

SERVER = settings.mongo_db_server
init(SERVER)

LOGLEVEL = settings.logging_level
logging.getLogger(__name__).setLevel(LOGLEVEL)

app = typer.Typer(help="Daily Scrum Telegram Bot CLI", no_args_is_help=True)

app.add_typer(user_app, name="user")


@app.command(name="start", help="Start telegram bot")
def start():
    ds_bot = DailyScrumBot(token=settings.telegram_bot_token)
    typer.echo("Starting Bot...")
    ds_bot.run()
