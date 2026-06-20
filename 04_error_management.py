from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIError,RateLimitError

load_dotenv()

client_wrong_key=OpenAI(api_key="2") # API KEY appositamente sbagliata per triggerare errore
client=OpenAI()

default_model="gpt-4.1-mini"
message="Ciao, il collo non è arrivato"

def classify(client,text):
    try:
        response=client.responses.create(
            model=default_model,
            input=text,
            instructions="Sei un classificatore di ticket. rispondi con una sola parola tra: tecnico, spedizione, generale."
        )
        return response.output_text

    except AuthenticationError as e:
        return f"Errore autenticazione: {e}"

    except RateLimitError as e:
        return f"Rate limit: {e}"

    except APIError as e:
        return f"Errore API: {e}"
    

result=classify(client,message)
print(result)

result_wrong_key=classify(client_wrong_key,message)
print(result_wrong_key)
