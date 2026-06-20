from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI()

default_model="gpt-4.1-mini"
message="Ciao, non mi è arrivato il collo"
instructions='''
Sei un classificatore di ticket. Devi ritornare il messaggio in questo formato: Priorità: [alta/bassa/media] - Tipologia: [tecnico,spedizione,fatturazione,generale] - messaggio
Priorità e Tipologia devono essere dedotte dal messaggio, metti Tipologia: generale se non rientra in una delle altre.
'''

response=client.responses.create(
    model=default_model,
    input=message,
    instructions=instructions
)

print(response.output_text)