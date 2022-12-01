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
async def mens6(ctx):

    mens6 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens6.add_field(name='US Sizing:', value='6M', inline=False)
    mens6.add_field(name='US Sizing:', value='7.5W', inline=False)
    mens6.add_field(name='UK Sizing:', value='5.5', inline=False)
    mens6.add_field(name='EU Sizing:', value='38.5', inline=False)
    mens6.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens6)

@bot.command()
async def mens6p5(ctx):

    mens6p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens6p5.add_field(name='US Sizing:', value='6.5M', inline=False)
    mens6p5.add_field(name='US Sizing:', value='8.0W', inline=False)
    mens6p5.add_field(name='UK Sizing:', value='6.0', inline=False)
    mens6p5.add_field(name='EU Sizing:', value='39.0', inline=False)
    mens6p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens6p5)

@bot.command()
async def mens7(ctx):

    mens7 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens7.add_field(name='US Sizing:', value='7M', inline=False)
    mens7.add_field(name='US Sizing:', value='8.5W', inline=False)
    mens7.add_field(name='UK Sizing:', value='6.0', inline=False)
    mens7.add_field(name='EU Sizing:', value='40.0', inline=False)
    mens7.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens7)

@bot.command()
async def mens7p5(ctx):

    mens7p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens7p5.add_field(name='US Sizing:', value='7.5M', inline=False)
    mens7p5.add_field(name='US Sizing:', value='9.0W', inline=False)
    mens7p5.add_field(name='UK Sizing:', value='6.5', inline=False)
    mens7p5.add_field(name='EU Sizing:', value='40.5', inline=False)
    mens7p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens7p5)

@bot.command()
async def mens8(ctx):

    mens8 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens8.add_field(name='US Sizing:', value='8M', inline=False)
    mens8.add_field(name='US Sizing:', value='9.5W', inline=False)
    mens8.add_field(name='UK Sizing:', value='7.0', inline=False)
    mens8.add_field(name='EU Sizing:', value='41.0', inline=False)
    mens8.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens8)

@bot.command()
async def mens8p5(ctx):

    mens8p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens8p5.add_field(name='US Sizing:', value='8.5M', inline=False)
    mens8p5.add_field(name='US Sizing:', value='10.0W', inline=False)
    mens8p5.add_field(name='UK Sizing:', value='7.5', inline=False)
    mens8p5.add_field(name='EU Sizing:', value='42.0', inline=False)
    mens8p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens8p5)

@bot.command()
async def mens9(ctx):

    mens9 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens9.add_field(name='US Sizing:', value='9M', inline=False)
    mens9.add_field(name='US Sizing:', value='10.5W', inline=False)
    mens9.add_field(name='UK Sizing:', value='8.0', inline=False)
    mens9.add_field(name='EU Sizing:', value='42.5', inline=False)
    mens9.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens9)

@bot.command()
async def mens9p5(ctx):

    mens9p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens9p5.add_field(name='US Sizing:', value='9M', inline=False)
    mens9p5.add_field(name='US Sizing:', value='11.0W', inline=False)
    mens9p5.add_field(name='UK Sizing:', value='8.5', inline=False)
    mens9p5.add_field(name='EU Sizing:', value='43.0', inline=False)
    mens9p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens9p5)

@bot.command()
async def mens10(ctx):

    mens10 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens10.add_field(name='US Sizing:', value='10M', inline=False)
    mens10.add_field(name='US Sizing:', value='11.5W', inline=False)
    mens10.add_field(name='UK Sizing:', value='9.0', inline=False)
    mens10.add_field(name='EU Sizing:', value='44.0', inline=False)
    mens10.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens10)

@bot.command()
async def mens10p5(ctx):

    mens10p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens10p5.add_field(name='US Sizing:', value='10.5M', inline=False)
    mens10p5.add_field(name='US Sizing:', value='12.0W', inline=False)
    mens10p5.add_field(name='UK Sizing:', value='9.5', inline=False)
    mens10p5.add_field(name='EU Sizing:', value='44.5', inline=False)
    mens10p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens10p5)

@bot.command()
async def mens11(ctx):

    mens11 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens11.add_field(name='US Sizing:', value='11M', inline=False)
    mens11.add_field(name='US Sizing:', value='12.5W', inline=False)
    mens11.add_field(name='UK Sizing:', value='10.0', inline=False)
    mens11.add_field(name='EU Sizing:', value='45.0', inline=False)
    mens11.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens11)

@bot.command()
async def mens11p5(ctx):

    mens11p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens11p5.add_field(name='US Sizing:', value='11.5M', inline=False)
    mens11p5.add_field(name='US Sizing:', value='13.0W', inline=False)
    mens11p5.add_field(name='UK Sizing:', value='10.5', inline=False)
    mens11p5.add_field(name='EU Sizing:', value='45.5', inline=False)
    mens11p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens11p5)

@bot.command()
async def mens12(ctx):

    mens12 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens12.add_field(name='US Sizing:', value='12M', inline=False)
    mens12.add_field(name='US Sizing:', value='13.5W', inline=False)
    mens12.add_field(name='UK Sizing:', value='11.0', inline=False)
    mens12.add_field(name='EU Sizing:', value='46.0', inline=False)
    mens12.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens12)

@bot.command()
async def mens12p5(ctx):

    mens12p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens12p5.add_field(name='US Sizing:', value='12.5M', inline=False)
    mens12p5.add_field(name='US Sizing:', value='14.0W', inline=False)
    mens12p5.add_field(name='UK Sizing:', value='11.5', inline=False)
    mens12p5.add_field(name='EU Sizing:', value='47.0', inline=False)
    mens12p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens12p5)

@bot.command()
async def mens13(ctx):

    mens13 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens13.add_field(name='US Sizing:', value='13M', inline=False)
    mens13.add_field(name='US Sizing:', value='14.5W', inline=False)
    mens13.add_field(name='UK Sizing:', value='12.0', inline=False)
    mens13.add_field(name='EU Sizing:', value='47.5', inline=False)
    mens13.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens13)

@bot.command()
async def mens13p5(ctx):

    mens13p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens13p5.add_field(name='US Sizing:', value='13.5M', inline=False)
    mens13p5.add_field(name='US Sizing:', value='15.0W', inline=False)
    mens13p5.add_field(name='UK Sizing:', value='12.5', inline=False)
    mens13p5.add_field(name='EU Sizing:', value='48.0', inline=False)
    mens13p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens13p5)

@bot.command()
async def mens14(ctx):

    mens14 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens14.add_field(name='US Sizing:', value='14M', inline=False)
    mens14.add_field(name='US Sizing:', value='15.5W', inline=False)
    mens14.add_field(name='UK Sizing:', value='13.0', inline=False)
    mens14.add_field(name='EU Sizing:', value='48.5', inline=False)
    mens14.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens14)

@bot.command()
async def mens14p5(ctx):

    mens14p5 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens14p5.add_field(name='US Sizing:', value='14.5M', inline=False)
    mens14p5.add_field(name='US Sizing:', value='16.0W', inline=False)
    mens14p5.add_field(name='UK Sizing:', value='13.5', inline=False)
    mens14p5.add_field(name='EU Sizing:', value='49.0', inline=False)
    mens14p5.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens14p5)

@bot.command()
async def mens15(ctx):

    mens15 = discord.Embed(title='Shoe Size Converter', color=0x070d53)
    mens15.add_field(name='US Sizing:', value='15M', inline=False)
    mens15.add_field(name='US Sizing:', value='16.5W', inline=False)
    mens15.add_field(name='UK Sizing:', value='14.0', inline=False)
    mens15.add_field(name='EU Sizing:', value='49.5', inline=False)
    mens15.set_footer(text='All shoe sizes are from https://www.nike.com/size-fit/mens-footwear .' , icon_url= 'https://imgur.com/zi8SCan.png')
    await ctx.send(embed=mens15)

@bot.command()
async def mens16(ctx):
    await ctx.send('Unfortunately, due to the limited number of people with shoe sizes 16 and above, I have decided not to make any conversions for this size or any size above 15.')


bot.run('MTAyODg3MjU4NDI5NDU4MDI0NQ.GkYlPA.9smFe6HPPIbhj3KcJYM68PsuqiYtcjiWnP9yUE')