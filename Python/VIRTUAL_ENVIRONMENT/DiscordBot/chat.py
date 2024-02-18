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
            

