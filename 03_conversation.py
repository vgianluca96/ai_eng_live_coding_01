from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI()

default_model="gpt-4.1-mini"
message="Spiegamela"

print("********************** Senza contesto")
response=client.responses.create(
    model=default_model,
    input=message
)

print(response.output_text)


conversation = [
    { "role": "user","content": "raccontami una barzelletta"},
    { "role": "assistant","content": "Perché il libro di matematica era triste? Perché aveva troppi problemi"},
    { "role": "user","content": "non l'ho capita, me la spieghi?"},
]

print("********************** Con contesto")
response=client.responses.create(
    model=default_model,
    input=conversation
)

print(response.output_text)