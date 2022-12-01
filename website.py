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
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hey! How are you doing today?')

@bot.command()
async def helpme(ctx):
    await ctx.send('For any inquiries or concern regarding my status, open up a ticket in Blizzard Notify and the developer will be with you right away!')

@bot.command()
async def info(ctx):
    await ctx.send('My name is Blizzard Bot. My goal is to ensure that all members of the Blizzard Notify community are able to navigate and find answers to their problems much quicker. I currently have a variety of features such as shoe size converter, website checker, and tips on certain websites. I am always in development with new features always being added.')



@bot.command()
async def footlocker(ctx):

    footlocker = discord.Embed(title='Website Checker', description='Footlocker is a Footsite. You can visit at https://www.footlocker.com/. ', color=0x070d53)
    footlocker.set_thumbnail(url='https://imgur.com/1Nl5Lc3.png')
    footlocker.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=footlocker)

@bot.command()
async def ftl(ctx):

    ftl = discord.Embed(title='Website Checker', description='Footlocker is a Footsite. You can visit at https://www.footlocker.com/. ', color=0x070d53)
    ftl.set_thumbnail(url='https://imgur.com/1Nl5Lc3.png')
    ftl.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=ftl)

@bot.command()
async def champssports(ctx):

    champssports = discord.Embed(title='Website Checker', description='Champs Sports is a Footsite. You can visit at https://www.champssports.com/. ', color=0x070d53)
    champssports.set_thumbnail(url='https://imgur.com/Blpctkl.png')
    champssports.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=champssports)

@bot.command()
async def champs(ctx):

    champs = discord.Embed(title='Website Checker', description='Champs Sports is a Footsite. You can visit at https://www.champssports.com/. ', color=0x070d53)
    champs.set_thumbnail(url='https://imgur.com/Blpctkl.png')
    champs.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=champs)

@bot.command()
async def amamaniere(ctx):

    amamaniere = discord.Embed(title='Website Checker', description='A Ma Maniere is a Shopify based website. You can visit at https://www.a-ma-maniere.com/. ', color=0x070d53)
    amamaniere.set_thumbnail(url='https://imgur.com/3Z4gQut.png')
    amamaniere.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=amamaniere)

@bot.command()
async def amm(ctx):

    amm = discord.Embed(title='Website Checker', description='A Ma Maniere is a Shopify based website. You can visit at https://www.a-ma-maniere.com/. ', color=0x070d53)
    amm.set_thumbnail(url='https://imgur.com/3Z4gQut.png')
    amm.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=amm)

@bot.command()
async def apb(ctx):

    apb = discord.Embed(title='Website Checker', description='APB Store is a Shopify based website. You can visit at https://www.apbstore.com/. ', color=0x070d53)
    apb.set_thumbnail(url='https://imgur.com/ipzaBQb.png')
    apb.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=apb)

@bot.command()
async def atmos(ctx):

    atmos = discord.Embed(title='Website Checker', description='Atmos or better known as Atmos USA is a Shopify based website. You can visit at https://www.apbstore.com/. ', color=0x070d53)
    atmos.set_thumbnail(url='https://imgur.com/1raKyWA.png')
    atmos.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=atmos)

@bot.command()
async def bbc(ctx):

    bbc = discord.Embed(title='Website Checker', description='BBC, yes its weird, dont think about it, or better known as BBCIceCream is a Shopify based website. You can visit at https://www.bbcicecream.com/. ', color=0x070d53)
    bbc.set_thumbnail(url='https://imgur.com/X7ni7kp.png')
    bbc.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=bbc)

@bot.command()
async def bodega(ctx):

    bodega = discord.Embed(title='Website Checker', description='Bodega is a Shopify based website. You can visit at https://bdgastore.com/. ', color=0x070d53)
    bodega.set_thumbnail(url='https://imgur.com/4m0RcDL.png')
    bodega.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=bodega)

@bot.command()
async def concepts(ctx):

    concepts = discord.Embed(title='Website Checker', description='Concepts is a Shopify based website. You can visit at https://cncpts.com/. ', color=0x070d53)
    concepts.set_thumbnail(url='https://imgur.com/6NDUkNN.png')
    concepts.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=concepts)

@bot.command()
async def cncpts(ctx):

    cncpts = discord.Embed(title='Website Checker', description='Concepts is a Shopify based website. You can visit at https://cncpts.com/. ', color=0x070d53)
    cncpts.set_thumbnail(url='https://imgur.com/6NDUkNN.png')
    cncpts.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=cncpts)

@bot.command()
async def dtlr(ctx):

    dtlr = discord.Embed(title='Website Checker', description='DTLR is a Shopify based website. You can visit at https://www.dtlr.com/. ', color=0x070d53)
    dtlr.set_thumbnail(url='https://imgur.com/q6IeJNg.png')
    dtlr.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=dtlr)

@bot.command()
async def dsmny(ctx):

    dsmny = discord.Embed(title='Website Checker', description='DSMNY is a Shopify based website. You can visit at https://shop-us.doverstreetmarket.com/. ', color=0x070d53)
    dsmny.set_thumbnail(url='https://imgur.com/qHwSRbo.png')
    dsmny.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=dsmny)

@bot.command()
async def darkside(ctx):

    darkside = discord.Embed(title='Website Checker', description='Darkside, or Darkside Initiative, is a Shopify based website. You can visit at https://www.thedarksideinitiative.com/. ', color=0x070d53)
    darkside.set_thumbnail(url='https://imgur.com/SA572Tk.png')
    darkside.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=darkside)

@bot.command()
async def dicks(ctx):

    dicks = discord.Embed(title='Website Checker', description='Dicks, or Dicks Sporting Goods, is neither a Shopify or a Footsite website. It is based on its own software. You can visit at https://www.dickssportinggoods.com/. ', color=0x070d53)
    dicks.set_thumbnail(url='https://imgur.com/Qd0EQdn.png')
    dicks.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=dicks)

@bot.command()
async def finishline(ctx):

    finishline = discord.Embed(title='Website Checker', description='FinishLine, is neither a Shopify or a Footsite website. It is based on its own software. You can visit at https://www.finishline.com/. ', color=0x070d53)
    finishline.set_thumbnail(url='https://imgur.com/McO0FtR.png')
    finishline.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=finishline)

@bot.command()
async def fnl(ctx):

    fnl = discord.Embed(title='Website Checker', description='FinishLine, is neither a Shopify or a Footsite website. It is based on its own software. You can visit at https://www.finishline.com/. ', color=0x070d53)
    fnl.set_thumbnail(url='https://imgur.com/McO0FtR.png')
    fnl.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=fnl)

@bot.command()
async def gbny(ctx):

    gbny = discord.Embed(title='Website Checker', description='GBNY is a Shopify based website. You can visit at https://gbny.com/. ', color=0x070d53)
    gbny.set_thumbnail(url='https://imgur.com/eVtufHJ.png')
    gbny.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=gbny)

@bot.command()
async def hibbett(ctx):

    hibbett = discord.Embed(title='Website Checker', description='Hibbett is neither a Shopify or a Footsite website. It is based on its own software. You can visit at https://www.hibbett.com/. ', color=0x070d53)
    hibbett.set_thumbnail(url='https://imgur.com/c7jxIIc.png')
    hibbett.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=hibbett)

@bot.command()
async def jdsports(ctx):

    jdsports = discord.Embed(title='Website Checker', description='JD Sports, is neither a Shopify or a Footsite website. It is based on its own software. You can visit at https://www.jdsports.com/. ', color=0x070d53)
    jdsports.set_thumbnail(url='https://imgur.com/jEODUuM.png')
    jdsports.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=jdsports)

@bot.command()
async def jd(ctx):

    jd = discord.Embed(title='Website Checker', description='JD Sports, is neither a Shopify or a Footsite website. It is based on its own software. You can visit at https://www.jdsports.com/. ', color=0x070d53)
    jd.set_thumbnail(url='https://imgur.com/jEODUuM.png')
    jd.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=jd)

@bot.command()
async def jimmyjazz(ctx):

    jimmyjazz = discord.Embed(title='Website Checker', description='Jimmy Jazz is a Shopify based website. You can visit at https://www.jimmyjazz.com/. ', color=0x070d53)
    jimmyjazz.set_thumbnail(url='')
    jimmyjazz.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=jimmyjazz)

@bot.command()
async def jj(ctx):

    jj = discord.Embed(title='Website Checker', description='Jimmy Jazz is a Shopify based website. You can visit at https://www.jimmyjazz.com/. ', color=0x070d53)
    jj.set_thumbnail(url='')
    jj.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=jj)

@bot.command()
async def kith(ctx):

    kith = discord.Embed(title='Website Checker', description='KITH is a Shopify based website. You can visit at https://kith.com/. ', color=0x070d53)
    kith.set_thumbnail(url='https://imgur.com/6whhp0U.png')
    kith.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=kith)

@bot.command()
async def lapstone(ctx):

    lapstone = discord.Embed(title='Website Checker', description='Lapstone, or Lapstone and Hammer is a Shopify based website. You can visit at https://www.lapstoneandhammer.com/. ', color=0x070d53)
    lapstone.set_thumbnail(url='https://imgur.com/YZF9utX.png')
    lapstone.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=lapstone)

@bot.command()
async def packer(ctx):

    packer = discord.Embed(title='Website Checker', description='Packer is a Shopify based website. You can visit at https://packershoes.com/. ', color=0x070d53)
    packer.set_thumbnail(url='https://imgur.com/CpEdDQY.png')
    packer.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=packer)

@bot.command()
async def size(ctx):

    size = discord.Embed(title='Website Checker', description='Size? is a Shopify based website. You can visit at https://size.ca/. ', color=0x070d53)
    size.set_thumbnail(url='https://imgur.com/joAhl6j.png')
    size.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=size)

@bot.command()
async def sneakerpolitics(ctx):

    sneakerpolitics = discord.Embed(title='Website Checker', description='Sneaker Politics is a Shopify based website. You can visit at https://sneakerpolitics.com/. ', color=0x070d53)
    sneakerpolitics.set_thumbnail(url='https://imgur.com/dCrpi3b.png')
    sneakerpolitics.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=sneakerpolitics)

@bot.command()
async def snkrpol(ctx):

    snkrpol = discord.Embed(title='Website Checker', description='Sneaker Politics is a Shopify based website. You can visit at https://sneakerpolitics.com/. ', color=0x070d53)
    snkrpol.set_thumbnail(url='https://imgur.com/dCrpi3b.png')
    snkrpol.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=snkrpol)

@bot.command()
async def saintalfred(ctx):

    saintalfred = discord.Embed(title='Website Checker', description='Saint Alfred is a Shopify based website. You can visit at https://www.saintalfred.com/. ', color=0x070d53)
    saintalfred.set_thumbnail(url='https://imgur.com/9okJ3sC.png')
    saintalfred.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=saintalfred)

@bot.command()
async def shoepalace(ctx):

    shoepalace = discord.Embed(title='Website Checker', description='Shoe Palace is a Shopify based website. You can visit at https://www.shoepalace.com/. ', color=0x070d53)
    shoepalace.set_thumbnail(url='https://imgur.com/ZcyrJ79.png')
    shoepalace.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=shoepalace)

@bot.command()
async def sp(ctx):

    sp = discord.Embed(title='Website Checker', description='Shoe Palace is a Shopify based website. You can visit at https://www.shoepalace.com/. ', color=0x070d53)
    sp.set_thumbnail(url='https://imgur.com/ZcyrJ79.png')
    sp.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=sp)

@bot.command()
async def shopnicekicks(ctx):

    shopnicekicks = discord.Embed(title='Website Checker', description='Shop Nice Kicks is a Shopify based website. You can visit at https://shopnicekicks.com/. ', color=0x070d53)
    shopnicekicks.set_thumbnail(url='https://imgur.com/TGHew8v.png')
    shopnicekicks.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=shopnicekicks)

@bot.command()
async def snk(ctx):

    snk = discord.Embed(title='Website Checker', description='Shop Nice Kicks is a Shopify based website. You can visit at https://shopnicekicks.com/. ', color=0x070d53)
    snk.set_thumbnail(url='https://imgur.com/TGHew8v.png')
    snk.set_footer(text='@BlizzardNotify | Powered by Blizzard Notify', icon_url='https://imgur.com/zi8SCan.png')
    await ctx.send(embed=snk)


bot.run('MTAyODg3MjU4NDI5NDU4MDI0NQ.GkYlPA.9smFe6HPPIbhj3KcJYM68PsuqiYtcjiWnP9yUE')