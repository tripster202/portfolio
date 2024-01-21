import requests

base_url = 'https://api.exchange.coinbase.com/'

response = requests.request('GET',base_url+'products')

print(response.json())