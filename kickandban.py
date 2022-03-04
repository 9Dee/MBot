import discord
from discord.ext import commands
from disnake import Member
from lightbulb import CommandErrorEvent, MissingRequiredPermission

class kickandban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        if reason == None:
            reason=" No reason"
        await ctx.guild.kick(member)
        await ctx.send(f"{member.mention} has been kicked for: {reason}")

    @kick.error
    async def kick_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to do that lol.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        if reason == None:
            reason=" No reason"
        await ctx.guild.ban(member)
        await ctx.send(f"{member.mention} has been banned for: {reason}")

    @ban.error
    async def ban_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to do that lol.")


def setup(bot: commands.Bot):
    bot.add_cog(kickandban(bot))
