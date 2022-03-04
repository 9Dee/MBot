import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Your bot has successfully connected!")

bot.load_extension("somecommands")

bot.load_extension("embeds")

bot.load_extension("kickandban")

bot.load_extension("fun")

bot.run('OTQ0NzYxMTc0OTM3OTg5MjAy.YhGTaA.4Dp4PY8CJEBov8yJCaH948StwXM')