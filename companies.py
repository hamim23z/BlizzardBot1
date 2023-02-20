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
    
@bot.command()
async def vcc(ctx):

    vcc = discord.Embed(title='Reliable Virtual Credit Card Providers', description='Virtual Credit Cards are used for botting in order to create multiple accounts and multiple tasks. They do work and are very effective. \n \n1. Privacy Card: https://privacy.com/ \n2. Revolut Card: https://www.revolut.com/en-US/cards/ \n3. Capital One: https://www.capitalone.com/digital/eno/virtual-card-numbers/ \n4. Slash Card: https://www.joinslash.com/ \n5. Stripe Card: https://stripe.com/issuing  ', color=0x070d53)
    vcc.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=vcc)
    
@bot.command()
async def nikeacc(ctx):

    nikeacc = discord.Embed(title='Nike Account Providers', description='Nike Accounts are used and bought by botters when they want to purchase something from Nike or Snkrs. These accounts are created and verified to make them seem entirely human. \n \n1. Swish Accounts: https://swishaccounts.com/ \n2. Lucky AIO: https://luckyaio.com/account-generator \n3. Boro Accounts: https://accounts.boroinc.com/ \n4. Swift Accounts: https://accountsbyswift.com/ \n5. Pookyy AIO: https://pookyyaccount.com/nike-accounts  ', color=0x070d53)
    nikeacc.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=nikeacc)

@bot.command()
async def shopifybot(ctx):

    shopifybot = discord.Embed(title='Top Tier Shopify Bots', description='Botting is taking over the sneaker game and there are a handful of bots that stand out from others in terms of overall success. Shopify sites release most items and Shopify bots are amongst the best. \n \n1. Valor AIO: https://valoraio.com/ \n2. Wrath: https://wrathbots.co/account \n3. Kodai AIO: https://kodai.io/ \n4. Prism AIO: https://prismaio.com/ \n5. NSB: https://www.nikeshoebot.com/  ', color=0x070d53)
    shopifybot.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=shopifybot)

@bot.command()
async def footsitesbot(ctx):

    footsitesbot = discord.Embed(title='Top Tier Footsite Bots', description='Botting is taking over the sneaker game and there are a handful of bots that stand out from others in terms of overall success. There are a few footsites and they release most pairs. \n \n1. NSB AIO: https://www.nikeshoebot.com/ \n2. Wrath AIO: https://wrathbots.co/account \n3. Kodai AIO: https://kodai.io/ \n4. Prism AIO: https://prismaio.com/ \n5. Ganesh AIO: https://ganeshbot.com/  ', color=0x070d53)
    footsitesbot.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=footsitesbot)

bot.run('TOKEN GOES HERE')
