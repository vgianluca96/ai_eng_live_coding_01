from dotenv import load_dotenv
from openai import OpenAI, APIError, AsyncOpenAI,AuthenticationError,RateLimitError
import json
import time
import asyncio
from pydantic import BaseModel

load_dotenv()

client=OpenAI()
client_async=AsyncOpenAI()

default_model="gpt-4.1-mini"
messages=[]
instructions="Sei un classificatore di ticket. Rispondi con una sola parola tra: spedizione, tecnico, fatturazione, generale"

class Ticket(BaseModel):
    id: int
    messaggio:str

def load_ticket():
    with open("tickets.json", encoding="utf-8") as f:
        data=json.load(f)
        return [Ticket(**d) for d in data]
    
def classify(text):
    try:
        response=client.responses.create(
            model=default_model,
            input=text,
            instructions=instructions
        )
        return response.output_text.strip().lower()

    except AuthenticationError as e:
        return f"Errore autenticazione: {e}"

    except RateLimitError as e:
        return f"Rate limit: {e}"

    except APIError as e:
        return f"Errore API: {e}"
    
async def classify_async(text):
    try:
        response=await client_async.responses.create(
            model=default_model,
            input=text,
            instructions=instructions
        )
        return response.output_text.strip().lower()

    except AuthenticationError as e:
        return f"Errore autenticazione: {e}"

    except RateLimitError as e:
        return f"Rate limit: {e}"

    except APIError as e:
        return f"Errore API: {e}"
    

async def in_parallel(tickets):
    return await asyncio.gather(*[classify_async(ticket.messaggio) for ticket in tickets])


tickets=load_ticket()

start=time.time()

results=[classify(t.messaggio) for t in tickets]
print("Risultato seriale: ", results, "in ", round(time.time()-start,2))


start=time.time()

results_parallel=asyncio.run(in_parallel(tickets))
print("Risultato parallelo: ", results_parallel, "in ", round(time.time()-start,2))