from openai import OpenAI 
from dotenv import dotenv_values

config = dotenv_values(".env")
model = OpenAI(api_key=config["KEY"])
