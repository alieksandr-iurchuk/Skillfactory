import requests
import json

from config import exchanger


class APIExteption(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise APIExteption('Слишком много (мало) параметров!')
        quote, base, amount = values

        if quote == base:
            raise APIExteption(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = exchanger[quote]
        except KeyError:
            raise APIExteption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = exchanger[base]
        except KeyError:
            raise APIExteption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExteption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        # r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=2ed5db14d81a7ab5ecf22ae758264507&symbol= {quote_ticker} & symbols = {base_ticker}')

        total_base = float(json.loads(r.content)[base_ticker])*amount


        return round(total_base, 3)