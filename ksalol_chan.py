import discord
from discord.ext import commands
from datetime import datetime
import token_helper
import version_helper
import responses
from legacy import client


KSALOL_SAMA = "https://raw.githubusercontent.com/maciejszulia/discordchan/master/ksalol-sama.png"
KSALOL_SAMA_BG = "https://raw.githubusercontent.com/maciejszulia/discordchan/master/ksalol-sama/ksalol-sama-background.png"
KSALOL_SAMA_LOCAL = "./ksalol-sama.png"


TOKEN = token_helper.get_token()
# WATCH OUT!
# print(f'TOKEN  = {tokenhelper.get_token()}')

VERSION = version_helper.get_version()
print(VERSION)
github_link = "github.com/maciejszulia/discordchan"

# current_time = datetime.datetime.now()
print("current_time =", datetime.now())

# Utwórz instancję klienta i zdefiniuj intencje
# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)

# # Funkcja uruchamiana przy starcie bota
# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} online at {datetime.now()}')   
    
#     # Znajdź kanał o nazwie "#test" na serwerze
#     channel = discord.utils.get(bot.get_all_channels(), name='test')

#     # if channel is not None:
#     #     await channel.send(
#     #         'online at ' + str(datetime.now()) + '\n' +
#     #         'current ver: ' + VERSION + '\n' +
#     #         KSALOL_SAMA_BG
#     #     )
#     # else:
#     #     print('channel not found')
        
# # Uruchom bota

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

async def send_msg(msg, user_msg, is_private):
    try:
        response = responses.get_response(user_msg)
        await msg.author.send(response) if is_private else await msg.channel.send(response)
        
    except Exception as e:
        print(e)
        pass
    
        
# bot.run(TOKEN)

def run_ksalol_sama():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} online at {datetime.now()}')  
        
    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            pass
        
        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)
        
        print(f'{username}: {user_msg} in {channel}')
        
        if user_msg[0] == '?':
            user_msg = user_msg[1:]
            await send_msg(msg, user_msg, is_private=True)
        else:
            await send_msg(msg,user_msg, is_private=False)
            
    
    
    bot.run("Nzc5MDAyNDA4MTAxNDc4NDAw.GrFDZD.CQ2tb1QYgR4Az_3cU50J1-KZxIbQaXW5hvm33A")