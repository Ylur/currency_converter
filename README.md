# currency_converter

1. Get API key (see: https://free.currencyconverterapi.com/free-api-key)

2. Add your API key in global environment variable CURRENCY_CONVERTER_API_KEY. For example:
    ```
    $ export CURRENCY_CONVERTER_API_KEY={ YOUR_KEY }
    ```

3. Run (use Python 3.6+):
    ```
    $ python3 converter.py 1
    ```
    Examples:
    ```
    $ python3 converter.py 1
    1 USD = 65.928038 RUB
    $ python3 converter.py 2
    2 USD = 131.856076 RUB
    $ python3 converter.py 100
    100 USD = 6592.8038 RUB
    ```
