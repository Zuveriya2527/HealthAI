import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATSON_API_KEY")
WATSON_URL = os.getenv("WATSON_URL")
PROJECT_ID = os.getenv("WATSON_PROJECT_ID")

# Get bearer token
def get_access_token():
    response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={
            "apikey": API_KEY,
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json().get("access_token")

# Send prompt to IBM Granite
def ask_granite(prompt, temperature=0.5, max_tokens=500):
    access_token = get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "model_id": "granite-13b-instruct-v2",
        "input": prompt,
        "parameters": {
            "decoding_method": "sample",
            "max_new_tokens": max_tokens,
            "min_new_tokens": 10,
            "temperature": temperature,
            "top_k": 50,
            "top_p": 1
        },
        "project_id": PROJECT_ID
    }

    url = f"{WATSON_URL}/ml/v1/text/generation"
    response = requests.post(url, headers=headers, json=data)

    try:
        return response.json()["results"][0]["generated_text"].strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
