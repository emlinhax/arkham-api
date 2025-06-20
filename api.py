import time
import json
import requests
import arkhash

def P(url):
    return (url, {"X-Payload": arkhash.generate_hash(url), "X-Timestamp": str(int(time.time()))})

// example
def get_balances(address):
    url, headers = P(f"https://api.arkm.com/balances/address/{address}")
    response = requests.get(url, headers=headers).json()
    return response
