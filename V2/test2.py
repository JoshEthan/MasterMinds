# https://pypi.org/project/websocket_client/
import websocket
import pandas as pd
import json
import schedule
import time
import os
from os import system

# HIT A LIMIT OF 50 STOCKS PER CONNECTION
# TODO - Try running multiple terminals. Also the data seems to be put onto the same df, so localize it.
#        We could also try different threads. Other than that, it is good to go. Maybe clean up the code some more.


df = pd.DataFrame({'Close': []})
close = 0
stock_dic = {}


print(stock_dic)


def job():
    global df
    print('\n\nAdding data to file...')
    for key in stock_dic:
        print(stock_dic[key])
        df = pd.concat(
            [df, pd.DataFrame({'Close': [stock_dic[key]]})], ignore_index=True)
        df.to_csv('oneMinStocks//' + key, index=False)
    print('Data added to files.')


def on_message(ws, message):
    time.sleep(5)
    # system('cls')
    print('\n\nGetting data...')
    msg = json.loads(message)
    global close
    # print(msg)
    close = msg['data'][0]['p']
    print('Data aquired...')
    schedule.run_pending()
    time.sleep(1)
    # print(msg['data'][0])
    print('Adding data to dictionary...')
    for data in msg['data']:
        for filename in os.listdir('Stocks'):
            stock_name = (filename).split('.')[0]
            if data['s'] == stock_name.upper():
                stock_dic[stock_name] = data['p']
    print(stock_dic)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    system('cls')
    i = 0
    print('Opening stocks...')
    # 7162 is too many to subscribe to; 101 too many; 51 yes; 76 too many; 61 too many;
    for filename in os.listdir('Stocks'):
        stock_name = (filename).split('.')[0].upper()
        print('Opened: ' + stock_name)
        ws.send('{"type":"subscribe","symbol":"'+stock_name+'"}')
        i += 1
        if i == 51:
            break


schedule.every(60).seconds.do(job)  # Add data to csv every TEN seconds

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0smcq748v6pgu5knkig",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
