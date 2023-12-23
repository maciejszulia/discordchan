import discord
import datetime
from discord import message
import random
import os
import token_helper


TOKEN = token_helper.get_token()

class MyClient(discord.Client):
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} online at {datetime.now()}')  

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
    async def on_ready(self):
        await discord.TextChannel.message.send('sram')
        
client = MyClient(intents=discord.Intents.default())
client.run(TOKEN)