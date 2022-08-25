from calendar import c
from email import header
from http import client, server
from click import pass_context
import discord
import random
import time
import typing as t
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import requests
import json

#:
# List[discord.SelectOption]):
#placeholder="Choose a catagory...", min_values=1, max_values=1, options=options)
#
#ion: discord.Interaction):
#
#
#
#t: Optional[float] = 120.0):
#imeout=timeout)
#
#

#------------------Variables------------------

hello = open('Files/Greetings.txt', 'r')
Greetings = hello.readlines()

quote = open('Files/Quotes.txt', 'r')
quotes = quote.readlines()

Author = open('Files/Author.txt', 'r')
Authors = Author.readlines()

with open('Files/kill.txt', 'r') as kill:
      killLines = kill.readlines()
      
roast = open('Files/Roasts.txt', 'r')
roasts = roast.readlines()

with open('Files/NeverEver.txt', encoding="utf8") as NeverEver:
      NeverHaveIEver = NeverEver.readlines()

Command = open('Files/Commands.txt', 'r')
Commands = Command.read()

compliment = open('Files/compliments.txt', 'r')
compliments = compliment.readlines()

Function = open('Files/Function.txt', 'r')
Functions = Function.read()

RanChoice = 0

mylist = 'Someone, (Haroon Wasnt bothered coding this part he will do this later)'

#------------------------------------

load_dotenv()

bot = commands.Bot(command_prefix='.')
bot.remove_command("help")

@bot.group(invoke_without_command=True)

#------------------------------------

@bot.event
async def on_ready():
      print('Logged in as ' + bot.user.name)
      print('id: ' + str(bot.user.id))
      print('------')
      print('Bot is online and ready to use')
      await bot.change_presence(activity=discord.Game(name='with my balls :)'))

#---------Help Command---------
@bot.command()
async def help(ctx):
          global Commands, Functions
          
          em = discord.Embed(title="List Of Commands", description="""~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
""" + random.choice(quotes) + "```.help```", color=discord.Color(0xd68e09))
          
          em.add_field(name="Commands", value=Commands, inline=True)
          em.add_field(name="Function", value=Functions, inline=True)
          
          await ctx.send(embed=em)


#------------------Hello Command------------------
@bot.command()
async def hello(ctx,
                #name: Options(str, "Hello"
                ):

          await ctx.reply(random.choice(Greetings))


#------------------Cum Command------------------
@bot.command()
async def cum(ctx): 
          await ctx.reply('Cum indeed.')


#------------------Gay Command------------------
@bot.command()
async def gay(ctx, name):
          if name == 'Harbane' or name == 'Haroon' or name == '@Harbane#6887' or name == 'Ahmad' or name == 'haroon' or name == 'harbane':
                    await ctx.reply('we have found that ' + name + ' is 100% gay and 100% gae')      
          else:
                    await ctx.reply(f'We have found that {name} is {random.randint(0, 100)}% gay.')
                  
                     
#------------------Gae Command------------------
@bot.command()
async def gae(ctx, name):
      await ctx.reply(f'We have found that {name} is {random.randint(0, 100)}% gae')

#------------------Quote Command------------------
@bot.command()
async def quote(ctx):  
          RanChoice = random.randint(0, len(quotes))
          print("Random quote is: " + str(RanChoice))
          em = discord.Embed(description=quotes[RanChoice] + """-""" + Authors[RanChoice], color=discord.Color(0xd68e09))
          await ctx.reply(embed=em)
          #view=view)


#------------------Kill Command------------------
@bot.command()
async def kill(ctx, *, name):
          global killLines
          await ctx.reply(f'{name} {random.choice(killLines)}')


#------------------Molest Command------------------
@bot.command()
async def molest(ctx, *, name):
          await ctx.reply('```Cuming Soon```')


#------------------Roast Command------------------
@bot.command()
async def roast(ctx, *, name):
      url = 'https://insult.mattbas.org/api/insult'

      headers = {
          'content-type': 'text/plain',
      }

      response = requests.get(url, headers=headers)
      print(str(response) + ' api request successfully')

      jokes=response.text
      
      await ctx.reply(name + """
""" + jokes 
      )
          
#------------------NeverHaveIEver Command------------------
@bot.command()
async def game1(ctx):
          await ctx.reply(f'```Never have I ever {random.choice(NeverHaveIEver)}```')

#------------------Commpliment Command------------------
@bot.command()
async def compliment(ctx, *, name):
          await ctx.reply(name + """
""" + random.choice(compliments)
 )

#------------------Moan Command------------------
@bot.command()
async def moan(ctx):
      if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('erro.mp3')
            player = voice.play(source)
            
      else:
            await ctx.send("You are not in vc, join vc and then do it dum")


#------------------Message Command------------------
@bot.command()
async def message(ctx, user:discord.User, *, message):
          await user.send(message)
      
   
#-----------------Magic 8 ball Command------------------
@bot.command()
async def ball(ctx, *, question): #question is the argument
        await ctx.reply(f'Your question is: {question}')
        time.sleep(2)
        await ctx.reply(f'hmm I am thinking..')
        time.sleep(1)
        await ctx.reply(random.choice(['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Yes', 'Signs point to yes', 'Concentrate and ask again', 'My reply is no', 'My sources say no', 'Very doubtful']))
        
            

#------------------Join Voice Call------------------

@bot.command(pass_context=True)
async def join(ctx):
      if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
      else:
            await ctx.send("You are not in vc, join vc and then do it dum")
            
#------------------Leave Voice Call------------------
@bot.command(pass_context=True)
async def leave(ctx):
      if (ctx.voice_client):
            if(ctx.author.voice):
                  await ctx.guild.voice_client.disconnect()
            else:
                  await ctx.send("You are not in vc")
      else:
            await ctx.send("me no in vc, dum")

bot.run(getenv('TOKEN'))