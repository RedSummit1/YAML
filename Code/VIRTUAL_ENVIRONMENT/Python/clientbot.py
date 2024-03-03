import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from OpenAi import Chat

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix = "!", intents=intents)


gpt = Chat()


@client.event
async def on_ready():
   print("The bot is now ready for use") 

testingServerID = 1197063979298725958


# This is the example slash command
#---------------------------------------------------------------------------------------------------------------------------------

@client.slash_command(name = "hello",description="Replies with hello", guild_ids=[testingServerID]) # name has to be lowercase
async def helloo(interaction: Interaction,text:str):
    await interaction.response.send_message("Hello I am ready to do whatever you want me to do. I got this {}".format(text))

@client.slash_command(name = "chat",description="Chat GPT in discord", guild_ids=[testingServerID]) # name has to be lowercase
async def chat(interaction: Interaction,text:str):
    await interaction.response.send_message(gpt.read(text))

#---------------------------------------------------------------------------------------------------------------------------------




client.run('MTIwNDk5NDg4OTkyMjY0NjA2Nw.G1BAFJ.S6e7KCsEH9hQvGvvqhWw0BWK6lhWeuHuLC66U8')





















