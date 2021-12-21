from beanie import Document


class UserModel(Document):
    telegram_id: int
    is_bot_admin: bool = False
