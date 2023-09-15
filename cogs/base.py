import discord
import ezcord
from discord.commands import slash_command


class Base(ezcord.Cog, emoji="🍪"):
    @slash_command(description="Hey")
    async def hey(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"Hey {ctx.user.mention}")


def setup(bot):
    bot.add_cog(Base(bot))
