import discord
from discord.ext import commands
import datetime
import tokenhelper
import versionhelper

TOKEN = tokenhelper.get_token()
print(tokenhelper.get_token())

version = versionhelper.get_version()
print(version)
github_link = str("github.com/maciejszulia/discordchan")

# current_time = datetime.datetime.now()
print("Aktualny czas:", datetime.datetime.now())

# Utwórz instancję klienta i zdefiniuj intencje
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)

# Funkcja uruchamiana przy starcie bota
@bot.event
async def on_ready():
    print(f'{bot.user.name} online at {datetime.datetime.now()}')   
    
    # Znajdź kanał o nazwie "#test" na serwerze
    channel = discord.utils.get(bot.get_all_channels(), name='test')

    if channel is not None:
        await channel.send(
            'online at ' + str(datetime.datetime.now()) + '\n' +
            'current ver: ' + version + '\n' +
            github_link
        )
    else:
        print('channel not found')
        

# Uruchom bota
bot.run(TOKEN)


