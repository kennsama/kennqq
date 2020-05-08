from discord.ext import commands
import random
import discord
import typing
ncolor= 0xFFD700



class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.snipe = {}

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        if not msg.content or msg.author.bot:
            return
        if not msg.channel.id in self.snipe:
            self.snipe[msg.channel.id] = []
        self.snipe[msg.channel.id].insert(0, msg)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        checks = [
            before.content == after.content,
            before.embeds != after.embeds and before.content == after.content,
            not after.content,
            before.pinned != after.pinned,
            before.author.bot
        ]
        if any(checks):
            return
        if not before.channel.id in self.snipe:
            self.snipe[before.channel.id] = []
        self.snipe[before.channel.id].insert(0, before)

    @commands.group(name='snipe', invoke_without_command=True)
    async def snipe(self, ctx, channel: typing.Optional[discord.TextChannel] = None, index: int = 0):
        if index < 0:
            return await ctx.send(":octagonal_sign: | **Invalid number!**")
        if not channel:
            channel = ctx.channel
        if ctx.channel.is_nsfw() is False and channel.is_nsfw() is True:
            return await ctx.send(":octagonal_sign: | **Nothing to snipe!** `owo`")
        if not channel.id in self.snipe:
            return await ctx.send(":octagonal_sign: | **Nothing to snipe!** `owo`")
        if len(self.snipe[channel.id]) - 1 < index:
            return await ctx.send(":octagonal_sign: | **Nothing to snipe!** `owo`")
        msg = self.snipe[channel.id][index]
        embed = discord.Embed(color=ncolor, description=msg.content)
        embed.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
        embed.set_footer(text=f"{index}/{len(self.snipe[channel.id]) - 1}")
        await ctx.send(embed=embed)

    @commands.command(name='reverse')
    async def uno_reverse(self, ctx, member: discord.Member):

        reverse_card = 'https://media.tenor.com/images/812b19ca9e2ab00039c215425011fc28/tenor.gif'
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{ctx.author.display_name} Has used reverse on {member.display_name}!")
        embed.set_image(url=reverse_card)
        if ctx.author.id == member.id:
            await ctx.send(f'{ctx.author.mention} Tried to reverse themselves!! cringe.')
        else:
            await ctx.send(embed=embed)

    @uno_reverse.error
    async def reverse_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                reverse_card = 'https://media.tenor.com/images/812b19ca9e2ab00039c215425011fc28/tenor.gif'
            embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
            embed.set_author(name=f"{ctx.author.display_name} Has used reverse!")
            embed.set_image(url=reverse_card)
            await ctx.send(embed=embed)

    @commands.command(name='nou')
    async def uno_no_u(self, ctx):
        reverse_card = 'https://media.tenor.com/images/2f3f6a77d4a356d8a742d6c7696f4334/tenor.gif'
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.set_author(name=f"no u!")
        embed.set_image(url=reverse_card)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def mock(self, ctx, *, mocktxt: str = None):
        if mocktxt is None:
            await ctx.send('Nothing to mock!')
            return
        mockedtxt = ''.join([i.lower() if random.randint(1, 100) < 51 else i.upper() for i in mocktxt])
        await ctx.send(content=mockedtxt, file=discord.File("mock.gif"))

        
    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        responses = ['https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif',
                     'https://media1.tenor.com/images/116fe7ede5b7976920fac3bf8067d42b/tenor.gif',
                     'https://media.tenor.com/images/dc61bf036b96b9a321943493c55ad8a4/tenor.gif',
                     'https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif',
                     'https://media1.tenor.com/images/5466adf348239fba04c838639525c28a/tenor.gif',
                     'https://media1.tenor.com/images/282cc80907f0fe82d9ae1f55f1a87c03/tenor.gif']
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.title = f"{ctx.author.display_name} pets " f"{member.display_name} uwu!"
        embed.set_image(url=random.choice(responses))
        if ctx.author.id == member.id:
            await ctx.send(f'**{ctx.author.mention}** gave a pat to themselves :<')
        else:
            await ctx.send(embed=embed)

    @pat.error
    async def pat_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                await ctx.send("not sure who to pat.")
                
                
    @commands.command(name='banhammer')
    async def banhammer(self, ctx):
        ban_hammer = ['https://media2.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif',
                      'https://media1.giphy.com/media/Vh2c84FAPVyvvjZJNM/giphy.gif',
                      'https://media1.tenor.com/images/a97445946bd39cb5dbf1dc076c0ecf93/tenor.gif'
                      ]
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.set_author(name="Ban! Ban! Ban!")
        embed.set_image(url=random.choice(ban_hammer))
        await ctx.send(embed=embed)

    @commands.command(name='notfunny')
    async def not_funny(self, ctx):
        not_funny = 'https://img.fireden.net/co/image/1572/42/1572424466161.gif'
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.set_author(name="ha ha ha")
        embed.set_image(url=not_funny)
        await ctx.send(embed=embed)   
        
    @commands.command()
    async def punch(self, ctx, member: discord.Member):
        responses = ['https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446',
                     'https://i.pinimg.com/originals/8d/50/60/8d50607e59db86b5afcc21304194ba57.gif',
                     'https://pa1.narvii.com/5668/41102d6eba9ba3d2812ee4b25ef51ce911d3a0f3_hq.gif',
                     'https://media.tenor.com/images/b96f63d9382fe52cfe43feac4a8a40d6/tenor.gif',
                     'https://vignette.wikia.nocookie.net/powerlisting/images/1/17/Saitama_Megaton_Punch.gif']
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.title = f"{ctx.author.display_name} gave " f"{member.display_name} a smack!"
        embed.set_image(url=random.choice(responses))
        if ctx.author.id == member.id:
            await ctx.send(f'{ctx.author.mention} Punched themselves!! cringe.')
        else:
            await ctx.send(embed=embed)

    @punch.error
    async def punch_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                await ctx.send("Give me someone to punch!")

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        responses = ['https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif',
                     'https://media.tenor.com/images/b6d0903e0d54e05bb993f2eb78b39778/tenor.gif',
                     'https://media.giphy.com/media/qscdhWs5o3yb6/giphy.gif',
                     'https://25.media.tumblr.com/tumblr_ma7l17EWnk1rq65rlo1_500.gif',
                     'https://gifimage.net/wp-content/uploads/2017/10/hug-gif-anime-11.gif',
                     'https://thumbs.gfycat.com/GratefulComplexGlassfrog-size_restricted.gif']
        embed = discord.Embed(colour=ncolor, timestamp=ctx.message.created_at)
        embed.title = f"{ctx.author.display_name} gave " f"{member.display_name} a hug!"
        embed.set_image(url=random.choice(responses))
        if ctx.author.id == member.id:
            await ctx.send(f'**{ctx.author.mention}** Hugged themselves :<')
        else:
            await ctx.send(embed=embed)

    @hug.error
    async def hug_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                await ctx.send("hug who?")


    @commands.command(aliases=['pp', 'ppp'])
    async def mypp(self, ctx, member: discord.Member):
        responses = ['8D',
                     '8=D',
                     '8==D',
                     '8===D',
                     '8====D',
                     '8=====D',
                     '8======D',
                     '8=======D',
                     '8========D',
                     '8=========D',
                     '8==========D',
                     '8===========D',
                     '8=============D',
                     '8==============D',
                     '8===============D']
        embed = discord.Embed(color=ncolor)
        embed.title = f'{member.display_name}\'s pp'
        embed.description = f'{random.choice(responses)}'
        await ctx.send(embed=embed)

    @mypp.error
    async def mypp_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                responses = ['8D',
                             '8=D',
                             '8==D',
                             '8===D',
                             '8====D',
                             '8=====D',
                             '8======D',
                             '8=======D',
                             '8========D',
                             '8=========D',
                             '8==========D',
                             '8===========D',
                             '8============D',
                             '8=============D',
                             '8==============D',
                             '8===============D']
                embed = discord.Embed(color=ncolor)
                embed.title = f'{ctx.author.display_name}\'s pp'
                embed.description = f'{random.choice(responses)}'
                await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, question):
        await ctx.send(question)

    @commands.command(aliases=['as', 'a'])
    async def ask(self, ctx, *, question):
        responses = ['No.',
                     'Yes.',
                     'I don\'t know.',
                     'No not really.',
                     'Yes definitely.',
                     'Maybe.']
        await ctx.send(f'{random.choice(responses)}')

    @ask.error
    async def ask_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'question':
                await ctx.send("You didn't ask me anything! dummy.")

def setup(bot):
    bot.add_cog(FunCog(bot))
