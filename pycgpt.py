import requests
from dotenv import load_dotenv
import os
import argparse
import datetime

def secret():
    load_dotenv()

secret()

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="Code needed")
args = parser.parse_args()

openai_api_ep = "https://api.openai.com/v1/completions"
api_key = os.getenv('api_key')

timeStamp = "\n" + str(datetime.datetime.now())

postHeader = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

postData = {
    "model": "text-davinci-003",
    "prompt": f"{args.prompt}",
    "max_tokens": 200,
    "temperature": 0.5
}

response = requests.post(openai_api_ep, headers=postHeader, json=postData)

if response.status_code == 200:
    output = response.json()["choices"][0]["text"]
    print(output)
    with open("pycgpt.log", "a") as file:
        file.write(timeStamp)
        file.write(output)

else:
    print(f"Malformed/Invalid Response \nStatus Code: {str(response.status_code)}")
