import subprocess
import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/"

def run(command: str):
    args = command.split(" ")
    res = subprocess.run(args, capture_output=True, encoding='UTF-8')
    return res.stdout, res.stderr

def send(endpoint: str, http_verb: str = "GET", params: dict[str, any]|None = None) -> any:
    if http_verb == "GET":
        return requests.get(OLLAMA_API_URL + endpoint, data=json.dumps(params)).json()
    if http_verb == "POST":
        return requests.post(OLLAMA_API_URL + endpoint, data=json.dumps(params)).json()
    return {}
