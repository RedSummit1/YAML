# This example requires the 'message_content' intent.
from dotenv import dotenv_values
import discord

MY_GUILD = discord.Object(id=1200426642733027428)


class MyClient(discord.Client):
    #events
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.tree = app_commands.CommandTree(self)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
intents.message_content = True
config = dotenv_values('.env')
client = MyClient(intents=intents)
client.run(config['DISKEY'])
#class MyTree(dicord.app_commands.CommandTree):

@client.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')

