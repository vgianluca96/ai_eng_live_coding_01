from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI()

default_model="gpt-4.1-mini"
message="Ciao, raccontami brevemente la storia degli LLM"

response=client.responses.create(
    model=default_model,
    input=message,
    stream=True
)

for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta,end="",flush=True)