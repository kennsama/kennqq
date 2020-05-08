import discord
import random
from discord.ext import commands
from discord.utils import get
import os
import shutil

BOT_PREFIX = "/"

bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')

players = {}


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Property of Code 002 and Code 016'))
    print(f'{bot.user} has logged in.')

    
bot.run(os.environ['TOKEN'])
