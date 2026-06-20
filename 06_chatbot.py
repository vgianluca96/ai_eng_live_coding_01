from dotenv import load_dotenv
from openai import OpenAI, APIError

load_dotenv()

client=OpenAI()

default_model="gpt-4.1-mini"
messages=[]

print("Ciao sono il tuo asistente personale. Scivi 'esci' per terminare")


while True:
    text=input("Gianluca: ")

    if(text=="esci"):
        break

    messages.append({"role": "user", "content": text})

    response= ""

    print("Assistente: ", end="", flush=True)

    try:
        stream= client.responses.create(
            model=default_model,
            instructions="Sei un assistente personale. Rispondi in maniera concisa",
            input=messages,
            stream=True
        )
    
        for event in stream:
            if event.type=="response.output_text.delta":
                print(event.delta,end="",flush=True)
                response+=event.delta
        print()

        messages.append({"role": "assistant", "content": response})

    except APIError as e:
        print(f"Error: {e}")
        break