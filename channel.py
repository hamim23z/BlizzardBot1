from attr import field
import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module. There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Hello, I am online now')

@bot.command()
async def roles(ctx):

    roles = discord.Embed(title='Blizzard Buddy', description='We have a variety of roles, in order to get them head on over to <#796100677192646698> . ', color=0x070d53)
    roles.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=roles)

@bot.command()
async def rules(ctx):

    rules = discord.Embed(title='Blizzard Buddy', description='We have a variety of rules that must be followed or else there will be punishments, in order to see them head on over to <#803288575777046539> . ', color=0x070d53)
    rules.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=rules)

@bot.command()
async def perks(ctx):

    perks = discord.Embed(title='Blizzard Buddy', description='There are a lot of ways to earn rewards in this server. We have 3 different tiers of members and you can see how to earn them at <#809063163105771581> . ', color=0x070d53)
    perks.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=perks)

@bot.command()
async def helpme(ctx):

    helpme = discord.Embed(title='Blizzard Buddy', description='You can ask for help in the main chat or open up a ticket in <#915113507102523462> . ', color=0x070d53)
    helpme.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=helpme)

@bot.command()
async def footsites(ctx):

    footsites = discord.Embed(title='Blizzard Buddy', description='There is a full fledged guide on how to purchase from Footsites for both manual and botting users. It is located in <#940768957600784424> . ', color=0x070d53)
    footsites.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=footsites)

@bot.command()
async def nike(ctx):

    nike = discord.Embed(title='Blizzard Buddy', description='There is a full fledged guide on how to purchase from Nike and Snkrs for both manual and botting users. It is located in <#940768981395070986> . ', color=0x070d53)
    nike.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=nike)

@bot.command()
async def shopify(ctx):

    shopify = discord.Embed(title='Blizzard Buddy', description='There is a full fledged guide on how to purchase from Shopify for both manual and botting users. It is located in <#940769006200164402> . ', color=0x070d53)
    shopify.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=shopify)

@bot.command()
async def yeezysupply(ctx):

    yeezysupply = discord.Embed(title='Blizzard Buddy', description='There is a full fledged guide on how to purchase from YeezySupply for both manual and botting users. It is located in <#940769026848722955> . ', color=0x070d53)
    yeezysupply.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=yeezysupply)

bot.run('MTAyODg3MjU4NDI5NDU4MDI0NQ.GkYlPA.9smFe6HPPIbhj3KcJYM68PsuqiYtcjiWnP9yUE')