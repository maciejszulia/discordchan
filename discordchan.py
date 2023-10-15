import discord
from discord.ext import commands
import time
import datetime

version = "0.0.2"
github_link = "https://github.com/maciejszulia/discordchan"

# Pobierz aktualny czas i datę
current_time = datetime.datetime.now()

# Wyświetl aktualny czas
print("Aktualny czas:", current_time)

print(f'TOKEN = ')
TOKEN = input()

# Utwórz instancję klienta i zdefiniuj intencje
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Funkcja uruchamiana przy starcie bota
@bot.event
async def on_ready():
    print(f'{bot.user.name} online at {current_time}')
    
    # Znajdź kanał o nazwie "#test-1" na serwerze
    channel = discord.utils.get(bot.get_all_channels(), name='test-1')

    if channel is not None:
        await channel.send(
            'online at ' + str(current_time) + '\n'+
            'current ver: '+ version + '\n' +
            + github_link
            )
    else:
        print('channel not found')

@bot.command()
async def ping(ctx):
    # Odpowiedz "pong" w kanale "#test-1"
    channel = discord.utils.get(ctx.guild.channels, name='test-1')

    if channel is not None:
        await channel.send('pong')
# Uruchom bota
bot.run(TOKEN)
