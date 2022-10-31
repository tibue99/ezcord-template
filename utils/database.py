import aiosqlite

from config import DB


async def setup_db():
    async with aiosqlite.connect(DB) as db:
        await db.execute(
            """CREATE TABLE IF NOT EXISTS users (
            guild_id INTEGER,
            user_id INTEGER,
            coins INTEGER DEFAULT 0,
            PRIMARY KEY (guild_id, user_id)
            )"""
        )


async def check_member(user_id, guild_id):
    async with aiosqlite.connect(DB) as db:
        await db.execute("INSERT OR IGNORE INTO users (user_id, guild_id) VALUES (?,?)", (user_id, guild_id))
        await db.commit()


async def update_value(user_id, guild_id, amount, value="coins", result=False):
    await check_member(user_id, guild_id)

    async with aiosqlite.connect(DB) as db:
        await db.execute(
            f"UPDATE users SET {value} = {value} + {amount} WHERE user_id = ? AND guild_id = ?", (user_id, guild_id)
        )
        await db.execute(f"UPDATE users SET {value} = 0 WHERE {value} < 0")
        await db.commit()
        if result:
            async with db.execute(
                    f"SELECT {value} FROM users WHERE user_id = ? AND guild_id = ?", (user_id, guild_id)
            ) as cursor:
                result = await cursor.fetchone()
                return result[0]


async def set_value(user_id, guild_id, amount, value="coins"):
    await check_member(user_id, guild_id)
    async with aiosqlite.connect(DB, detect_types=1) as db:
        await db.execute(
            f"UPDATE users SET {value} = ? WHERE user_id = ? AND guild_id = ?", (amount, user_id, guild_id)
        )
        await db.commit()


async def get_value(user_id, guild_id, value="coins"):
    await check_member(user_id, guild_id)
    async with aiosqlite.connect(DB, detect_types=1) as db:
        async with db.execute(
            f"SELECT {value} FROM users WHERE user_id = ? AND guild_id = ?", (user_id, guild_id)
        ) as cursor:
            result = await cursor.fetchone()
            return result[0]
