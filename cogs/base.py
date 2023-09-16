import discord
import ezcord
from discord.commands import slash_command

from utils import dab


db = dab.UserDB()


class Base(ezcord.Cog, emoji="🍪"):
    @slash_command(description="Earn coins!")
    async def coins(self, ctx: discord.ApplicationContext):
        await db.add_coins(ctx.user.id, 100)
        new_bal = await db.get_coins(ctx.user.id)

        await ctx.respond(f"You earned **100** coins! You now have **{new_bal}** coins 🪙")


def setup(bot):
    bot.add_cog(Base(bot))
