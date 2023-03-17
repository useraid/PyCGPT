import requests
from dotenv import load_dotenv
import os

def secret():
    load_dotenv()

secret()

openai_api_ep = "https://api.openai.com/v1/completions"
api_key = os.getenv('api_key')

postHeader = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

postData = {
    "model": "text-davinci-003",
    "prompt": "Write a paragraph on how cats are better than dogs",
    "max_tokens": 200,
    "temperature": 0.5
}

response = requests.post(openai_api_ep, headers=postHeader, json=postData)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Malformed/Invalid Response \nStatus Code: {str(response.status_code)}")
