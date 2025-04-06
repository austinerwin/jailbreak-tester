import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def send_message_to_openrouter(message, model="openai/gpt-4o-mini", system_prompt=None):
    """
    Send a message to the OpenRouter model and return the response.

    Args:
    - message (str): The message to send to the OpenRouter model.
    - model (str): The model identifier, default is "openai/gpt-4o-mini".
    - system_prompt (str, optional): The system prompt to set the behavior or context for the assistant.

    Returns:
    - str: The content of the response from the model or an error message.
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "",
        "X-Title": "",
        "Content-Type": "application/json"
    }
    
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": message})
    
    data = json.dumps({
        "model": model,
        "messages": messages
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