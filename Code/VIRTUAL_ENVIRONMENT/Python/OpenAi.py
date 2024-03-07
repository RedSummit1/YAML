#../bin/python3
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
        Chat.cycle({"role":"user","content": " ".join(prompt)})
        output = self.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system", "content":"You're seething with anger!!"},
                *Chat.queue
            ],
        )

        Chat.cycle({"role":"assistant","content":output.choices[0].message.content})
        return Chat.queue[-1]["content"]

    def draw(self,*prompt):
        response = self.images.generate(
            model="dall-e-3",
            prompt=" ".join(prompt),
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        return image_url

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
