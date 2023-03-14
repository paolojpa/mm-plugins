from discord.ext import commands

from core.checks import thread_only

class Userid_lister(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @thread_only()
    async def userid(self, ctx):
        await ctx.send(ctx.thread.recipient.id)

async def setup(bot):
    await bot.add_cog(Userid_lister(bot))
