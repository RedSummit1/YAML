from openai import OpenAI as quarterinhere
import dotenv

config = dotenv.dotenv_values(".env")
print(config["KEY"])
