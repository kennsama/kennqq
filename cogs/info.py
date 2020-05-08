import discord
from discord.ext import commands
import random
ncolor= 0xFFD700
Guild = object()

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

class InfoCog(commands.Cog):

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.title = member.display_name
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @avatar.error
    async def avatar_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
                embed.title = ctx.author.display_name
                embed.set_image(url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        roles = list()
        for role in member.roles[1:]:
            roles.append(role)

        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Server name:", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Roles ({len(roles)})", value=f"\n".join([role.mention for role in roles]))
        embed.add_field(name="Top role:", value=member.top_role.mention)
        embed.add_field(name="Bot?", value=member.bot)
        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                roles = list()
                for role in ctx.author.roles[1:]:
                    roles.append(role)

                embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)

                embed.set_author(name=f"User Info - {ctx.author}")
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

                embed.add_field(name="ID:", value=ctx.author.id)
                embed.add_field(name="Server name:", value=ctx.author.display_name)

                embed.add_field(name="Created at:", value=ctx.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
                embed.add_field(name="Joined at:", value=ctx.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
                embed.add_field(name=f"Roles ({len(roles)})", value=f"\n".join([role.mention for role in roles]))
                embed.add_field(name="Top role:", value=ctx.author.top_role.mention)
                embed.add_field(name="Bot?", value=ctx.author.bot)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):
        try:
            toto = await ctx.channel.create_invite(max_uses=15)
            await ctx.send(f"https://discord.gg/{toto.code}")
        except Exception as error:
            await ctx.send(':octagonal_sign: | **I don\'t have permissions to create invite links!** `uwu`')


    @commands.command()
    async def serverinfo(self, ctx):
        server = ctx.message.guild

        online = 0
        for i in server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
        all_users = []
        for user in server.members:
            all_users.append('{}#{}'.format(user.name, user.discriminator))
        all_users.sort()

        channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
        vchannel_count = len([x for x in server.channels if type(x) == discord.channel.VoiceChannel])
        role_count = len(server.roles)
        emoji_count = len(server.emojis)

        embed = discord.Embed(color=ncolor, timestamp=ctx.message.created_at)
        embed.title = ctx.guild.name
        embed.add_field(name='Owner', value=server.owner, inline=False)
        embed.add_field(name='Members', value=server.member_count)
        embed.add_field(name='Currently Online', value=online)
        embed.add_field(name='Text Channels', value=str(channel_count))
        embed.add_field(name='Voice Channels', value=str(vchannel_count))
        embed.add_field(name='Region', value=server.region)
        embed.add_field(name='Verification Level', value=str(server.verification_level))
        embed.add_field(name='Number of roles', value=str(role_count))
        embed.add_field(name='Number of emotes', value=str(emoji_count))
        embed.add_field(name='Created At', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed.set_thumbnail(url=server.icon_url)
        embed.set_author(name='Server Info', icon_url=server.icon_url)
        embed.set_footer(text='Server ID: %s' % server.id)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoCog(bot))
