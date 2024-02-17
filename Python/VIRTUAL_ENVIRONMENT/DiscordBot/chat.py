#!../bin/python3
from openai import OpenAI 
from dotenv import dotenv_values

class Chat(OpenAI):
    def __init__(self):
        config = dotenv_values(".env")
        super().__init__(api_key=config["KEY"])
        print("Chat is online")

    def read(self,*prompt):
        output = self.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content":" ".join(prompt)}
            ]
        )
        print(output.choices[0].message.content)
            




#
#        completion = client.chat.completions.create(
#            model="gpt-3.5-turbo",
#            messages=[
#                {"role":"system", "content":"You are a helpful assistant."},
#                {"role":"user","content":"Hello!"}
#            ]
#        )

## Need to set intents properties for discord bot
#intents = discord.Intents.default()
#intents.message_content = True
#client = discord.Client(intents=intents)
#
## Discord bot event handlers (Will put in a class to organize code better)
#
#@client.event # Prints Online in terminal when bot instance is ready for deployment in server
#async def on_ready():
#    print("Online")
#
## Code to notify bot (chat) when to listen for prompt 
#bot = commands.Bot(command_prefix ="!",intents=intents)# Use "!" as symbol to notify bot to listen 
#@bot.command()
#async def chat(ctx,*arg):
## Code responsible for sending request to OpenAi api (feel free to pass in other arguements 
## docs: https://platform.openai.com/docs/api-reference/chat
#    completion =  instance.chat.completions.create(
#    model="gpt-3.5-turbo-1106",
#    messages = [
#            {
#              "role": "user",
#              "content": " ".join(arg)
#            }
#        ],
#    n=2,
#    )    
#
##performed a model dump which turns the model object to dictionary 
##docs: https://docs.pydantic.dev/latest/concepts/serialization/
#    response = completion.model_dump().get('choices')[0].get('message').get('content')
#    await ctx.send(response)
#
##Api key for bot 
#bot.run(config["DISCORD_KEY"])
#
#
