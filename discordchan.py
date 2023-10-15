import discord
from discord.ext import commands
import time

import datetime

# Pobierz aktualny czas i datę
current_time = datetime.datetime.now()

# Wyświetl aktualny czas
print("Aktualny czas:", current_time)


# Ustal token bota
TOKEN = 'Nzc5MDAyNDA4MTAxNDc4NDAw.Gi8Vzx.5XCLixJB4dP3B-ZynLhfOChvfI-dCP8SokDM2c'


# Utwórz instancję klienta i zdefiniuj intencje
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Funkcja uruchamiana przy starcie bota
@bot.event
async def on_ready():
    print(f'{bot.user.name} online at {current_time}')

# Dodaj komendę !witaj
# @bot.command()
# async def witaj(ctx):
#     # Pobierz kanał o nazwie "#test-1" na serwerze
#     channel = discord.utils.get(ctx.guild.channels, name='test-1')

#     if channel is not None:
#         await channel.send(f'Witaj, {ctx.author.mention} w kanale {channel.mention}!')
#     else:
#         await ctx.send('Kanał "#test-1" nie został znaleziony na serwerze.')

# Uruchom bota
bot.run(TOKEN)
