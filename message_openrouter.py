import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SITE_URL = os.getenv("SITE_URL")
SITE_NAME = os.getenv("SITE_NAME")

def send_message_to_openrouter(message, model="openai/gpt-4o-mini"):
    """
    Send a message to the OpenRouter model and return the response.

    Args:
    - message (str): The message to send to the OpenRouter model.
    - model (str): The model identifier, default is "openai/gpt-4o-mini".

    Returns:
    - str: The content of the response from the model or error message.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": SITE_URL,
        "X-Title": SITE_NAME,
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": message}]
    })
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=data
    )
    
    if response.status_code == 200:
        completion = response.json()
        return completion['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage:
response = send_message_to_openrouter("Hi", "openai/gpt-4o-mini")
print(response)
