from ast import arguments
import discord
from discord.ext import commands


class Embeds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def embed(self, ctx: commands.Context, arg: str):
        embed = discord.Embed(title=arg)
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Embeds(bot))
