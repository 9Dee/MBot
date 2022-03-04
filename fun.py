from ast import Await, Is
from concurrent.futures import process
from ctypes import resize
from multiprocessing import Event
from turtle import color
import discord
from discord.ext import commands
from disnake import Member
from PIL import Image, ImageFont, ImageDraw
import textwrap
from io import BytesIO

from lightbulb import command, has_role_permissions


class fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx: commands.Context, member: discord.Member):
        embed=discord.Embed(title="SLAPPED!", description = f"{member.mention} was slapped by" f'{ctx.author.mention} :fearful:',color=0xff820d) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/859218666625302549/946949908563374130/girl-slap.gif")
        await ctx.send(embed=embed)

    
    @commands.command()
    async def shoot(self: commands.Bot, ctx: commands.Context, member: discord.Member=None):
        if commands.Bot == member.mention:
            await ctx.send("I'm bulletproof dumbass")
            return

        if member==None:
            member=ctx.author
            embed=discord.Embed(title="Uh-Oh!", description = f"{ctx.author.mention} killed themself because they didnt mention someone to shoot!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/859218666625302549/948370972413673484/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f7474306f49725a326a315f4445513d3d2d3730343936393335342e31353861373362666230613533326164363038383633.gif")
            await ctx.send(embed=embed)
            return
            
        embed=discord.Embed(title="BANG!", description = f"{ctx.author.mention} Brutally killed" f'{member.mention}!')
        embed.set_image(url="https://cdn.discordapp.com/attachments/859218666625302549/948366831352156160/anime-shooting.gif")
        await ctx.send(embed=embed)
        return
    
def setup(bot: commands.Bot):
    bot.add_cog(fun(bot))
