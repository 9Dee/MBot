from email.mime import image
from logging.config import listen
import discord
from discord.ext import commands
from disnake import Embed
from hikari import EmbedImage, Member
from lightbulb import NotOwner 

class SomeCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)} ms :ping_pong:")
        
    @commands.command()
    @commands.is_owner()
    async def setstatus(self, ctx: commands.Context, *, text:str):
        await self.bot.change_presence(activity=discord.Game(name=text))

    @setstatus.error
    async def setstatus_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.NotOwner):
            await ctx.send("Error: You are not the owner!")

    @commands.command()
    @commands.is_owner()
    async def setstatus2(self, ctx: commands.Context, *, text:str):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))

    @setstatus2.error
    async def setstatus2_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.NotOwner):
            await ctx.send("Error: You are not the owner!")
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message
    
    @commands.command()
    async def snipe(self, ctx: commands.Context):
        if not self.last_msg:
            await ctx.send("There are no messages to snipe!")
            return
        
        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title="Sniped! "f'{author}', description=content)
        embed.set_author(name="Caught in 4k")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/859218666625302549/946209564276162581/scope-gallery-counter-strike-wiki-fandom-powered-wikia-31.png")
        embed.set_footer(text="sniped by: {}".format (ctx.author.display_name))
        await ctx.send(embed=embed)


    @commands.command()
    @commands.is_owner()
    async def creator(self, ctx: commands.Context):
        embed = discord.Embed (title= "9''' Management Bot Creator", description= "Creator of 9''' Management Bot", color=0xDB0CBB, )
        embed.set_image(url="https://cdn.discordapp.com/attachments/859218666625302549/946193462846427226/giphy_1.gif")
        embed.set_author(name="9Dee#0082", icon_url= ctx.author.avatar_url)
        await ctx.send (embed=embed)

    @commands.command()
    async def avatar(self, ctx, *, avamember : discord.Member=None) -> None:
        avamember = avamember or ctx.author
        embed=discord.Embed (title=f"{avamember.display_name}\'s Avatar")
        embed.set_image(url=avamember.avatar_url)
        await ctx.send (embed=embed)

   
  

    


def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))
