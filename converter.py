import logging
import sys
from typing import Optional

from client import get_current_exchange_rate

logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def convert_value(dollars_count: float) -> Optional[float]:
    exchange_rate = get_current_exchange_rate()
    if exchange_rate is None:
        return None
    return exchange_rate * dollars_count


def main():
    try:
        value = float(sys.argv[1])
    except (ValueError, IndexError):
        logging.warning('Incorrect input')
        print('Input value is incorrect')
    else:
        new_value = convert_value(value)
        if new_value is not None:
            logging.info('Success')
            print(f'{value} USD = {new_value} RUB')
        else:
            logging.warning('Exchange rate not received')
            print('Current exchange rate not received')


if __name__ == '__main__':
    main()
