import asyncio
import typer
from daily_scrum_bot.data import init

from daily_scrum_bot.data.models import UserModel
from daily_scrum_bot.settings import get_settings

app = typer.Typer(help="Manage bot users", no_args_is_help=True)

settings = get_settings()
SERVER = settings.mongo_db_server


@app.command(
    name="list",
    help="List users telegrams ids",
)
def list():
    async def list_users():
        await init(SERVER)
        users = UserModel.find_all()
        first = True
        async for user in users:
            if not first:
                typer.echo("")
            else:
                first = False
            typer.echo(
                f"Name: {user.name}\nTelegram Id: {user.telegram_id}\nIs Bot Admin: {user.is_bot_admin}"
            )

    asyncio.run(list_users())


@app.command(
    name="add",
    help="Add user",
)
def add(
    name: str,
    telegram_id: int,
    is_bot_admin: bool = False,
):
    async def add_user(
        name: str,
        telegram_id: int,
        is_bot_admin: bool = False,
    ):
        await init(SERVER)
        new_user = UserModel(
            name=name,
            telegram_id=telegram_id,
            is_bot_admin=is_bot_admin,
        )
        await new_user.insert()

    asyncio.run(
        add_user(
            name,
            telegram_id,
            is_bot_admin=is_bot_admin,
        )
    )
