import os

import requests

API_URL = 'https://free.currencyconverterapi.com/api/v6/convert'
API_KEY = os.environ['CURRENCY_CONVERTER_API_KEY']
REQUEST_PAYLOAD = {
    'q': 'USD_RUB',
    'apiKey': API_KEY,
    'compact': 'ultra',
}


def convert_value(value):
    r = requests.get(url=API_URL, params=REQUEST_PAYLOAD)

    exchange_rate = r.json()['USD_RUB']
    return exchange_rate * value
