from beanie import Document


class UserModel(Document):
    name: str
    telegram_id: int
    is_bot_admin: bool = False
