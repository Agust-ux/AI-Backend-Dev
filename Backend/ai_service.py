import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "answer": response.choices[0].message.content,
        "tokens": response.usage.total_tokens
    }