import json
import requests
name = 'Bitcoin'.lower()
res = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids='
                   f'{name}&vs_currencies=usd&include_market_cap=true&include_24hr_change=true')

print(res.json())