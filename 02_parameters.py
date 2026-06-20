from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI()

default_model="gpt-4.1-mini"
message="Ciao, non mi è arrivato il collo"
instructions="Classifica il ticket con una sola parola. "
temperature=0
max_output_tokens=40

print(f'****************** parametro temperatura: {temperature}')
for n in range(3):
    response=client.responses.create(
        model=default_model,
        input=message,
        instructions=instructions,
        temperature=temperature
    )

    print(response.output_text)


print(f'****************** parametro max_output_tokens: {max_output_tokens}')
response=client.responses.create(
    model=default_model,
    input="Raccontami l'odissea",
    max_output_tokens=max_output_tokens
)

print(response.output_text)