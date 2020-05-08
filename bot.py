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




bot.run(os.environ['TOKEN'])
