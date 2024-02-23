import discord
import ezcord

from utils import dab


class Bot(ezcord.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), language="en")

        self.load_cogs()
        self.add_help_command()
        self.add_status_changer(
            "Ezcord",
            discord.Game("on {guild_count} servers"),
            discord.Activity(type=discord.ActivityType.watching, name="{coins} coins"),
            coins=dab.UserDB().get_all_coins,
        )


if __name__ == "__main__":
    bot = Bot()
    bot.run()
