import requests
r = requests.get('https://finnhub.io/api/v1/crypto/symbol?exchange=binance&token=c0smcq748v6pgu5knkig')
print(r.json())
