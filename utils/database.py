import ezcord


class UserDB(ezcord.DBHandler):
    def __init__(self):
        super().__init__("user.db")

    async def setup(self):
        await self.exec(
            """CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            coins INTEGER DEFAULT 0
            )"""
        )

    async def add_coins(self, user_id, amount):
        async with self.start() as cursor:
            await cursor.exec("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
            await cursor.exec(
                "UPDATE users SET coins = coins + ? WHERE user_id = ?",
                (amount, user_id),
            )

    async def get_users(self):
        return await self.all("SELECT user_id, coins FROM users")

    async def get_coins(self, user_id):
        return await self.one("SELECT coins FROM users WHERE user_id = ?", (user_id,))
