import discord
import random
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil

BOT_PREFIX = "/"

bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')

players = {}

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('with depression'))
    print('Bot is online.')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left.')

@bot.command()
async def bully(ctx):
    await ctx.send('HAHA SHORT KOGO')

@bot.command()
async def facebook(ctx):
    await ctx.send('https://www.facebook.com/xrebby')

@bot.command()
async def poweroff(ctx):
    await ctx.send('Shutting down.\nSayonara.')

@bot.command()
async def twitter(ctx):
    await ctx.send('https://www.twitter.com/keeenn__')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency * 1000)}ms.')

@bot.command()
async def info(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Nine iota",
        description="This bot is on beta"
    )

    embed.set_author(name="Ken Sama", icon_url="https://pbs.twimg.com/media/EVEhwkKU4AMrnz0?format=jpg&name=900x900")
    embed.set_image(url="https://pbs.twimg.com/media/EVEhwkKU4AMrnz0?format=jpg&name=900x900")
    embed.set_thumbnail(url="https://pbs.twimg.com/media/EVEhwkKU4AMrnz0?format=jpg&name=900x900")
    embed.add_field(name="Twitter", value="https://www.twitter.com/keeenn__", inline=False)
    embed.add_field(name="Facebook", value="https://www.facebook.com/xrebby", inline=False)
    embed.add_field(name="Beta", value="0.0.2", inline=False)

    embed.set_footer(text="kawaii")

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
        author = ctx.message.author

        test_e = discord.Embed(
            colour=discord.Colour.orange()
        )
        test_e.set_author(name="Bot prefix = /")
        test_e.add_field(name="Facebook Link", value="https://www.facebook.com/xrebby", inline=False)
        test_e.add_field(name="Twitter Link", value="https://www.twitter.com/keeenn__")

        await author.send(embed=test_e)

        await ctx.send("A direct message has been sent.")


@bot.command(aliases=['as', 'a'])
async def ask(ctx, *, question):
    responses = ['No',
                 'Yes',
                 'I don\'t know.',
                 'No not really.',
                 'Yes definitely.',
                 'Maybe.']
    await ctx.send(f'{random.choice(responses)}')

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


bot.run('Njk2MjM5NTkxNzIzNzYxNjk2.XosxEQ.l9isIIHWP4Y8PjmSaO9NvdxM3b8')
