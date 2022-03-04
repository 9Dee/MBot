import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.getenv("OTQ0NzYxMTc0OTM3OTg5MjAy.YhGTaA.mT7iWa7Mfm3JcPVBXAO3C4NxeIg")

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Your bot has successfully connected!")

bot.load_extension("somecommands")

bot.load_extension("embeds")

bot.load_extension("kickandban")

bot.load_extension("fun")

bot.run("OTQ0NzYxMTc0OTM3OTg5MjAy.YhGTaA.mT7iWa7Mfm3JcPVBXAO3C4NxeIg")