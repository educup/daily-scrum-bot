import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from daily_scrum_bot.data.models import UserModel


async def init(db_url: str):
    client = AsyncIOMotorClient(db_url)
    await init_beanie(
        database=client.db_name,
        document_models=[
            UserModel,
        ],
    )
