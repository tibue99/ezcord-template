import discord
import ezcord


class Bot(ezcord.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), language="en")

        self.load_cogs()
        self.add_help_command()


if __name__ == "__main__":
    bot = Bot()
    bot.run()
