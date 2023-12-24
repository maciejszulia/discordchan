import discord
import datetime
import random
import os
from token_helper import get_token

token = get_token()

class MyClient(discord.Client):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    async def on_ready(self):
        print(f'{self.user.name} online at {datetime.datetime.now()}')
        channel = self.get_channel(779002907709145088)
        
        if channel:
            await channel.send('chuj')
        else:
            print(f"Channel with ID {channel} not found.")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

client = MyClient(intents=discord.Intents.default())
client.run(token)
