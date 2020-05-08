from discord.ext import commands
import discord
import json
import os

ncolor = 0xFFD700

def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        return prefixes[str(message.guild.id)]
    except Exception as Error:
        return '%'

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)

bot.remove_command("help")

@bot.event
async def on_message(message):
    channel = bot.get_channel(705360157470752839)
    if message.guild is None:
        await channel.send(message.content + f'\n-{message.author}')
    await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '%'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Property of Code 002 and Code 016'))
    print(f'{bot.user} has logged in.')
    bot.load_extension('cogs.info')
    bot.load_extension('cogs.fun')


@bot.command()
async def changeprefix(ctx, prefix):
    if ctx.author.id == 398275064765874186:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f':octagonal_sign: | **Prefix changed to `{prefix}`**')
    else:
        await ctx.send("`YOU HAVE NO PERMISSIONS`")



@bot.group(name='help', invoke_without_command=True)
async def help(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]
    embed = discord.Embed(colour=ncolor)
    embed.set_author(name=f"Commands for {bot.user.display_name}", icon_url=bot.user.avatar_url)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="**Commands**", value=f"`{prefix}help commands`")
    embed.add_field(name="**Music**", value=f"`{prefix}help music`")
    embed.add_field(name="**Fun**", value=f"`{prefix}help fun`")
    embed.add_field(name="**Info**", value=f"`{prefix}help info`")
    await ctx.send(embed=embed)


@help.command(name='music')
async def submusic(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]
    embed = discord.Embed(colour=ncolor)
    embed.title = 'Music Commands'
    embed.description = f'`{prefix}join`\nJoin the user\'s voice channel\n\n' \
                        f'`{prefix}leave`\nLeave the voice channel\n\n' \
                        f'`{prefix}play [song]`\nAdd a song to queue or plays it if the queue is empty\n\n' \
                        f'`{prefix}search [song]`\nSearch for a song\n\n' \
                        f'`{prefix}pause`\n Pause the player\n\n' \
                        f'`{prefix}shuffle`\nShuffle the queue\n\n' \
                        f'`{prefix}stop`\nStop the player\n\n' \
                        f'`{prefix}volume [vol]`\nAdjust the player\'s volume\n\n' \
                        f'`{prefix}bassboost [1-3]`\nChange bassboost level. `0` to turn it off\n\n' \
                        f'`{prefix}queue`\nDisplay the queued tracks\n\n' \
                        f'`{prefix}remove`\nRemove a song from the queue\n\n' \
                        f'`{prefix}loop`\nLoop the current playing song\n\n' \
                        f'`{prefix}skip`\n Skip the song\n\n' \
                        f'`{prefix}seek [seconds]`\nChange the current track\'s position\n\n'
    await ctx.send(embed=embed)

@help.command(name='fun')
async def subfun(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]
    embed = discord.Embed(colour=ncolor)
    embed.title = 'Fun commands'
    embed.description = f'`{prefix}mypp`\npp size macine owo\n\n' \
                        f'`{prefix}punch`\npunch someone!\n\n' \
                        f'`{prefix}hug`\nhug someone uwu\n\n' \
                        f'`{prefix}ask`\nanswers yes or no questions\n\n' \
                        f'`{prefix}say`\nmake the bot say anything you want\n\n'
    await ctx.send(embed=embed)


@help.command(name='info')
async def subinfo(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]
    embed = discord.Embed(colour=ncolor)
    embed.title = 'Info (sub commands)'
    embed.description = f'`{prefix}info owner`\nServer owner\n\n' \
                        f'`{prefix}info channel`\nChannel info\n\n' \
                        f'`{prefix}info members`\nMember info\n\n' \
                        f'`{prefix}info role`\nRole info\n\n'
    await ctx.send(embed=embed)


@help.command(name='commands')
async def helpcommands(ctx):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]
    embed = discord.Embed(colour=ncolor)
    embed.title = 'Bot commands'
    embed.description = f'`{prefix}serverinfo`\nget server info\n\n' \
                        f'`{prefix}userinfo [user]`\nget user info\n\n' \
                        f'`{prefix}avatar [user]`\nshows the user\'s avatar\n\n' \
                        f'`{prefix}ping`\nbot latency\n\n' \
                        f'`{prefix}invite`\ncreate a invite link for the server'

    await ctx.send(embed=embed)


@bot.group(name='info', invoke_without_command=True)
async def info(ctx):
    facebook = 'https://www.twitter.com/keeenn__'
    twitter = 'https://www.facebook.com/xrebby'
    discord_link = 'https://discord.gg/DsPdEwD'
    embed = discord.Embed(colour=ncolor)
    embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
    embed.set_image(url=bot.user.avatar_url)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="**Facebook**", value=f"[Facebook Link]({facebook})")
    embed.add_field(name="**Twitter**", value=f"[Twitter Link]({twitter})")
    embed.add_field(name="**Discord**", value=f"[Discord Support]({discord_link})", inline=False)
    embed.add_field(name="**Owner**", value=f"`Code 016#6167`", inline=False)
    embed.add_field(name=f'**{bot.user.display_name}**',
                    value=f"{bot.user.display_name} is a fun bot that can play music and "
                          "retrieve user/server informations.", inline=False)
    embed.add_field(name='**Version**', value="0.0.2", inline=False)
    embed.set_footer(text="this bot is in development.")
    await ctx.send(embed=embed)


@info.command(name='channel')
@commands.guild_only()
async def channel(ctx, channel: discord.TextChannel = None):
    if not channel:
        channel = ctx.channel
    embed = discord.Embed(colour=ncolor)
    embed.title = 'Channel info'
    embed.add_field(name="Channel Name", value=channel.name)
    embed.add_field(name="ID", value=channel.id)
    embed.add_field(name="Type", value=channel.type)
    embed.add_field(name="Created", value=channel.created_at)
    embed.add_field(name="Topic", value=channel.topic)
    embed.add_field(name='NSFW', value=channel.is_nsfw())
    await ctx.send(embed=embed)


@info.command(name='owner')
@commands.guild_only()
async def owner(ctx):
    owner: discord.Member = ctx.message.guild.owner

    roles = list()
    for role in owner.roles[1:]:
        roles.append(role)

    embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
    embed.title = "Server Owner"
    embed.add_field(name="Display name", value=owner.mention)
    embed.set_thumbnail(url=owner.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=owner.id)
    embed.add_field(name="Server name:", value=owner.display_name)

    embed.add_field(name="Created at:", value=owner.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=owner.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=f"Roles ({len(roles)})", value=f"\n".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=owner.top_role.mention)
    await ctx.send(embed=embed)


@info.command(name='role')
@commands.guild_only()
async def role(ctx, role: discord.Role):
    embed = discord.Embed(title='Role Info', color=role.color)
    embed.add_field(name='Name', value=role.name)
    embed.add_field(name='ID', value=role.id, inline=False)
    embed.add_field(name='Users in this role', value=str(len(role.members)))
    embed.add_field(name='Hex value', value=str(role.color))
    embed.add_field(name='RGB value', value=role.color.to_rgb())
    embed.add_field(name='Mentionable', value=role.mentionable)
    embed.add_field(name="Position", value=role.position)
    embed.add_field(name='Created at', value=role.created_at.__format__('%x at %X'))
    embed.set_thumbnail(url='http://www.colorhexa.com/{}.png'.format(str(role.color).strip("#")))
    await ctx.send(content=None, embed=embed)

@info.command(name='members')
@commands.guild_only()
async def members(ctx):
    onlines = 0
    bots = 0
    server = ctx.message.guild
    for member in server.members:
        if member.bot is True:
            bots += 1
        elif member.status != discord.Status.offline:
            onlines += 1

    embed = discord.Embed(
        title="{}".format(ctx.message.guild.name),
        color=ncolor)
    embed.add_field(name="Members", value=str(len(server.members)))
    embed.add_field(name="Online", value=str(onlines))
    embed.add_field(name="Humans", value=str(len(server.members) - bots))
    embed.add_field(name="Bots", value=str(bots))
    embed.set_thumbnail(url=server.icon_url)
    try:
        return await ctx.send(embed=embed)

    except discord.HTTPException:
        pass


@bot.command()
@commands.is_owner()
async def clear(ctx, amount=5):
    try:
        await ctx.channel.purge(limit=amount + 1)
    exept Exception as Error:
        await ctx.send("No permission to delete user messages!")



@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=ncolor)
    ping = (f'{round(bot.latency * 1000)}ms.')
    embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="**Bot Latency**", value=":signal_strength: " + ping)
    await ctx.send(embed=embed)


@bot.command()
async def gen(ctx, *, question):
    channel = bot.get_channel(695945711690186763)
    await channel.send(question)
    print(question + f"\n-{ctx.author}")


@bot.command()
async def msg(ctx, *, question):
    channel = bot.get_channel(695945711690186763)
    await channel.send(question + f"\n-{ctx.author}")
    print(question + f"\n-{ctx.author}")


@bot.command()
@commands.is_owner()
async def yuk(ctx, *, question):
    channel = bot.get_channel(703575747050078208)
    await channel.send(question)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned!')
        print(f'{member} has been banned!')
    except Exception as e:
        await ctx.send("Failed to ban:" + e)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked!')
        print(f'{member} has been kicked!')
    except Exception as failkick:
        await ctx.send("Failed to kick:" + str(failkick))


@bot.event
async def on_member_join(member):
    print(f'{member} has joined.')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left.')
    
    
bot.run(os.environ['TOKEN'])
