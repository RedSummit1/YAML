#!../bin/python3
import discord 
from dotenv import dotenv_values

class MyClient(discord.Client):
    async def on_ready(self):
            print("Hello my name is {}!".format(self.user))
        

        






intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
config = dotenv_values(".env")
client.run(config['DISKEY'])
