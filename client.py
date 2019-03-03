import logging
import os
from http import HTTPStatus
from typing import Optional

import requests
from requests import RequestException

API_URL = 'https://free.currencyconverterapi.com/api/v6/convert'
API_KEY = os.environ['CURRENCY_CONVERTER_API_KEY']
REQUEST_PAYLOAD = {
    'q': 'USD_RUB',
    'apiKey': API_KEY,
    'compact': 'ultra',
}


def get_current_exchange_rate() -> Optional[float]:
    try:
        response = requests.get(url=API_URL, params=REQUEST_PAYLOAD)
    except RequestException:
        logging.error('An exception occurred while handling a request.')
        return

    if response.status_code != HTTPStatus.OK:
        logging.warning('Response status code not success')
        return

    data = response.json()
    if data:
        return data.get('USD_RUB')
