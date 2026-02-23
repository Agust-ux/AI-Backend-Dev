import os #lese miljøvariabler
from openai import OpenAI #AI klient
from dotenv import load_dotenv #les .env-filen

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# os.getenv() henter variabel fra .env
# OpenAI lager klient
# API-nøkkel brukes for autentisering

def ask_ai(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

# Dette gjør selve AI-kallet:
#   Modell: "gpt-4o-mini"
#   Vi sender én melding
#   AI svarer

    return {
        "answer": response.choices[0].message.content,  #teksten AI-en svarte
        "tokens": response.usage.total_tokens           #Hvor mange tokens som ble brukt (viktig for logging og kostnad).
    }

if __name__ == "__main__":
    result = ask_ai("Si hei pa norsk")
    print(result)

    print(os.getenv("OPENAI_API_KEY"))