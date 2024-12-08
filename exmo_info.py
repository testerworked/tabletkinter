import requests
import time
import hmac
import hashlib

API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

def get_market_info():
    url = 'https://api.exmo.com/v1.1/pair_settings/'
    response = requests.get(url)
    return response.json()

def get_balance():
    url = 'https://api.exmo.com/v1.1/user_info/'
    nonce = str(int(time.time() * 1000))
    params = {
        'nonce': nonce
    }
    sign = hmac.new(API_SECRET.encode(), urlencode(params).encode(), hashlib.md5).hexdigest()
    headers = {
        'Key': API_KEY,
        'Sign': sign
    }
    response = requests.post(url, params=params, headers=headers)
    return response.json()

if __name__ == '__main__':
    market_info = get_market_info()
    print("Market Info:", market_info)

    balance_info = get_balance()
    print("Balance Info:", balance_info)