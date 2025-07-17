import requests
from utils.config import OPENROUTER_KEY, OPENROUTER_API_URL, DEFAULT_MODEL

def call_openrouter(messages: list, model: str = DEFAULT_MODEL, max_tokens=800, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    response = requests.post(OPENROUTER_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"OpenRouter Error {response.status_code}: {response.text}")


#OPENROUTER_API_KEY=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
