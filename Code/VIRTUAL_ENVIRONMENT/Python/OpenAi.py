#!../bin/python3
from openai import OpenAI 
from dotenv import dotenv_values

class Chat(OpenAI):

    queue = [] 

    @classmethod
    def cycle(cls,message):
       cls.queue.append(message)


    def __init__(self):
        config = dotenv_values("./.env")
        super().__init__(api_key=config["OPEN_AI_KEY"])
        print("Chat is online")

    def read(self,*prompt):
        response = ""
        Chat.cycle({"role":"user","content": " ".join(prompt)})




        output = self.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":"You are a helpful assistant."},
                *Chat.queue
                #{"role":"user","content":" ".join(prompt)}
            ],
            stream=True,
        )
        for chunk in output:
            block = chunk.choices[0].delta.content
            print(block if block else "\n",end="",flush=True)
            response += block if block else ""

        Chat.cycle({"role":"assistant","content":response})

       # .choices[0].message.content)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
