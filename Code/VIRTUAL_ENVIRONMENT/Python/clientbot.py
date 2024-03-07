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

testingServerID = 1200426642733027428


# This is the example slash command
#---------------------------------------------------------------------------------------------------------------------------------

@client.slash_command(name = "chat",description="Chat GPT in discord", guild_ids=[testingServerID]) # name has to be lowercase
async def chat(interaction: Interaction,text:str):
    await interaction.response.send_message(gpt.read(text))

@client.slash_command(name = "draw",description="DALLE in discord", guild_ids=[testingServerID]) # name has to be lowercase
async def draw(interaction: Interaction,text:str):
    await interaction.response.defer(ephemeral=True)
    image_url = gpt.draw(text)
    await interaction.followup.send(image_url)
    #await interaction.response.send_message(image_url)

#---------------------------------------------------------------------------------------------------------------------------------

    



client.run('MTIxMzY5NzQ0MDE0NjkxNTQyOA.GnR5Wz.zP0QaMXUwbOuoVw8iy0CSaY88BUkmJRwh1uvuQ')
