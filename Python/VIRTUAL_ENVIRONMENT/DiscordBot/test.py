#!../bin/python3

from openai import OpenAI 
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(api_key=config["KEY"])

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content":"You are a helpful assistant."},
        {"role":"user","content":"Hello!"}
    ]
)

print(completion.choices[0].message.content)



