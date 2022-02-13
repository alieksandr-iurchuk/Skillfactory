import json
import requests
from extensions import APIExteption, Converter

# r = Converter.get_price("рубль", "доллар", "100")
r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=2ed5db14d81a7ab5ecf22ae758264507')
total_base = float(json.loads(r.content)['rates'][base_ticker])*amount
print(total_base)

# (json.loads(r.content)["rates"]["USD"])
# r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key \n'
#                  f'=2ed5db14d81a7ab5ecf22ae758264507&symbols=USD,AUD,CAD,PLN,MXN&format=1')
# http://api.exchangeratesapi.io/v1/latest?access_key=2ed5db14d81a7ab5ecf22ae758264507&base={quote_ticker}&symbols={base_ticker}