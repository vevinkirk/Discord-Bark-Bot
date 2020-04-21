#bot.py
import os
import discord
from discord.ext import commands

#for sports data
from sportsreference.nba.teams import Teams
from sportsreference.nba.schedule import Schedule

#for rss feeds
import feedparser

bot = commands.Bot(command_prefix='$', description='A bot that does a little bit of everything')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bark Bot", description="A bot that does a little bit of everything", color=0xeee657)
    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$dog", value="Gives a cute dog gif to lighten up the mood.", inline=False)
    embed.add_field(name="$nba", value="Prints out all NBA teams", inline=False)
    embed.add_field(name="$nba_schedule LAL ", value="Prints out the schedule for team, input team abbreviation i.e LAL for Los Angeles Lakers", inline=False)
    embed.add_field(name="$rss_feed URL", value="Prints out the latest entries given from a valid rss feed", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bark Bot", description="A bot that does a little bit of everything!", color=0xeee657)

    #give info about you here
    embed.add_field(name="Author", value="virkthejerk")
    
    #shows the number of servers the bot is a member of
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

#General Commands
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def dog(ctx):
    await ctx.send("https://media.giphy.com/media/mCRJDo24UvJMA/source.gif")

#NBA Commands
@bot.command()
async def nba(ctx):
    teams = Teams()
    for team in teams:
        await ctx.send((team.name, team.abbreviation))

@bot.command()
async def nba_schedule(ctx, a):
    #todo - convert to uppercase and regex check for 3characters, print error if wrong
    team_schedule = Schedule(a)
    for game in team_schedule:
        await ctx.send((game.date,game.result,game.opponent_abbr,game.boxscore_index))

#Finance Commands
@bot.command()
async def rss_feed(ctx, url):
    #to do check if valid url, regex check for url
    d = feedparser.parse(url)
    limit = len(d.entries)
    if limit > 10:
        limit = 10
    for i in range(0, limit):
        item = d.entries[i]
        name = item.title
        link = item.link
        await ctx.send((name,link))

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))

