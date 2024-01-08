import discord
import datetime
from token_helper import get_token
import asyncio

token = get_token()

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        intents = kwargs.pop('intents', discord.Intents.default())
        intents.message_content = True
        super().__init__(*args, intents=intents, **kwargs)

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name=f"jebac zydow at {datetime.datetime.now()}"))
        print(f'{self.user.name} online at {datetime.datetime.now()}')
        channel_id = 779002907709145088  # Replace with your channel ID
        channel = self.get_channel(channel_id)
        
        if channel:
            print(f"{datetime.datetime.now()}: At: channel with ID {channel}")

            # Fetch the last 5 messages in the channel
            async def get_messages():
                return [message async for message in channel.history(limit=5)]
            
            messages = await asyncio.gather(get_messages())

            # Print the content of each message
            for message in messages[0]:
                pass
                # await channel.send(f"Message from {message.author}: {message.content}")

client = MyClient()
client.run(token)
