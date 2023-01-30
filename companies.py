from attr import field
import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module. There are a number of utility commands being showcased here.'''

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Hello, I am online now')

@bot.command()
async def proxies(ctx):

    proxies = discord.Embed(title='Prime Proxy Companies', description='These are the best proxies in the sneaker game right now and they have proven success for many releases. This is not a sponsorship or partnership.\n \n1. Oculus Proxies: https://oculusproxies.com/#/home \n2. Live Proxies: https://liveproxies.io/ \n3. Donut Proxies: https://www.donutproxy.com/home \n4. Leaf Proxies: https://www.leafproxies.com/ \n5. Diamond Proxies: https://www.diamondproxy.net/  ', color=0x070d53)
    proxies.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=proxies)

bot.run('TOKEN GOES HERE')
