# import pandas as pd


# df = pd.DataFrame({'Close': [121.63, 123.02]})
# print(df)
# df.to_csv('test.csv', index=False)

import time
import schedule
import json
import pandas as pd
import requests
from os import system
import os

# FAILED ATTEMPT TO USE 'Quote' FROM FINNHUB, IT WOULDN'T ALLOW MORE THAN ONE IN A MINUTE...


r = requests.get(
    'https://finnhub.io/api/v1/quote?symbol=A&token=c0smcq748v6pgu5knkig')
print(r.json())


df = pd.DataFrame({'Close': []})
close = 0


# def job():
#     global df
#     df = pd.concat([df, pd.DataFrame({'Close': [close]})], ignore_index=True)
#     df.to_csv('oneMinStocks//aa.us.txt', index=False)

for filename in os.listdir('oneMinStocks'):
    stock_name = (filename).split('.')[0]
    print('Stock Name: ', stock_name)
    r = requests.get(
        'https://finnhub.io/api/v1/quote?symbol='+stock_name+'&token=c0smcq748v6pgu5knkig')
    print(r.json())


# def on_message(ws, message):
#     msg = json.loads(message)
#     global close
#     close = msg['data'][0]['p']
#     schedule.run_pending()
#     time.sleep(1)
#     print(msg['data'][0])
#     for data in msg['data']:
#         print(data)
