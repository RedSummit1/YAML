import nextcord
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
   print("The bot is now ready for use") 

testingServerID = 1200426642733027428


# This is the example slash command
#---------------------------------------------------------------------------------------------------------------------------------

@client.slash_command(name = "hello",description="Replies with hello", guild_ids=[testingServerID]) # name has to be lowercase
async def helloo(interaction: Interaction,text:str):
    await interaction.response.send_message("Hello I am ready to do whatever you want me to do. I got this {}".format(text))

#---------------------------------------------------------------------------------------------------------------------------------




client.run('MTIxMzY5NzQ0MDE0NjkxNTQyOA.GvIC2S.dtK_QxOyBN-2xDisocjXuv5AusY38JYNDo1T90')





















