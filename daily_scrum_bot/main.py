from typing import Optional
import typer

from daily_scrum_bot.commands import user_app

app = typer.Typer(help="Daily Scrum Telegram Bot CLI", no_args_is_help=True)

app.add_typer(user_app, name="user")


@app.command(name="start", help="Start telegram bot")
def start():
    typer.echo("Starting Bot...")
