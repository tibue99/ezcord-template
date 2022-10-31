import discord
from discord.ext import commands

import os

from utils import *


class Bot(discord.Bot):
    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(
            intents=intents,
            debug_guilds=None
        )

        self.load_cogs()

    def load_cogs(self) -> None:
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                self.load_extension(f'cogs.{filename[:-3]}')

    async def on_ready(self):
        print(f"{self.user} is online ({discord.__version__})")
        await dab.setup_db()

    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            seconds = ctx.command.get_cooldown_retry_after(ctx)
            await ctx.respond(
                embed=discord.Embed(
                    title="Cooldown",
                    description=f"Try again in `{convert_time(seconds)}`.",
                    color=discord.Color.red()
                ),
                ephemeral=True
            )
        else:
            await ctx.respond(
                embed=discord.Embed(
                    title="Error",
                    description=f"The following error occurred: ```{error}```",
                    color=discord.Color.red()
                ),
                ephemeral=True
            )
            raise error

    def run(self):
        super().run(os.getenv("TOKEN"))
