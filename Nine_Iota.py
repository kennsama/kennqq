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

@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)

        if voice is not None:
            return await voice.move_to(channel)

        await channel.connect()

        print(f"The bot has connected to {channel}\n")
        await ctx.send(f"Joined {channel}.")

@bot.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}.")
    else:
        print("Bot is not in a channel")
        await ctx.send("Don't think I'm in a voice channel.")

@bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, *url: str):
        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print("No more queued song(s)\n")
                    queues.clear()

                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                if length != 0:
                    print("Song done, playing next queued\n")
                    print(f"Songs still in queue: {still_q}")
                    song_there = os.path.isfile("song.mp3")
                    if song_there:
                        os.remove("song.mp3")
                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, 'song.mp3')

                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 1

                else:
                    queues.clear()
                    return

            else:
                queues.clear()
                print("No songs were queued before the ending of the last song\n")


        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                queues.clear()
                print("Removed old song file")
        except PermissionError:
            print("Bot is being played")
            await ctx.send("Currently playing.\nPls use /queue")
            return

        Queue_infile = os.path.isdir("./Queue")
        try:
            Queue_folder = "./Queue"
            if Queue_infile is True:
                print("Removed old Queue Folder")
                shutil.rmtree(Queue_folder)
        except:
            print("No old Queue folder")

        await ctx.send("Getting music.")

        voice = get(bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': "./song.mp3",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        song_search = " ".join(url)

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading audio now\n")
                ydl.download([f"ytsearch1:{song_search}"])
        except:
            print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
            c_path = os.path.dirname(os.path.realpath(__file__))
            system("spotdl -ff song -f " + '"' + c_path + '"' + " -s " + song_search)

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

        await ctx.send(f"Playing " + song_search + ".")
        print("Playing\n")

@bot.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Paused.")
    else:
        print("Not playing")
        await ctx.send("Not playing.")

@bot.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed")
        voice.resume()
        await ctx.send("Resumed.")
    else:
        print("Not paused")
        await ctx.send("Not paused.")

@bot.command(pass_context=True, aliases=['s', 'stp'])
async def stop(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    queues.clear()

    queue_infile = os.path.isdir("./Queue")
    if queue_infile is True:
        shutil.rmtree("./Queue")

    if voice and voice.is_playing():
        print("Stopped")
        voice.stop()
        await ctx.send("Stopped.")
    else:
        print("Not playing")
        await ctx.send("Not playing.")

queues = {}

@bot.command(pass_context=True, aliases=['n', 'skip'])
async def next(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)


    if voice and voice.is_playing():
        print("Skipping")
        voice.stop()
        await ctx.send("Skipping.")
    else:
        print("Failed")
        await ctx.send("Failed.")

queues = {}

@bot.command(pass_context=True, aliases=['q', 'que'])
async def queue(ctx, *url: str):
    await ctx.send("Adding to queue.")
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    song_search = " ".join(url)

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([f"ytsearch1:{song_search}"])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        q_path = os.path.abspath(os.path.realpath("Queue"))
        system(f"spotdl -ff song{q_num} -f " + '"' + q_path + '"' + " -s " + song_search)


    await ctx.send(song_search + " added to queue.")

@bot.command(pass_context=True, aliases=['v', 'vol'])
async def volume(ctx, volume: int):

        if ctx.voice_client is None:
            return await ctx.send("Not connected to any voice channel.")

        print(volume / 100)

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Volume set to {volume}%.")

bot.run('Njk2MjM5NTkxNzIzNzYxNjk2.XosxEQ.l9isIIHWP4Y8PjmSaO9NvdxM3b8')
