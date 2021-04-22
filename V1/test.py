# https://pypi.org/project/websocket_client/
import websocket
import pandas as pd
import json
pd.set_option('display.max_columns', 5)
df = pd.DataFrame(columns=['Trade Conditions',
                           'Last Price', 'Symbol', 'Time', 'Volume'])

# type: Message Type
# data: List of trades or price updates
# s: Symbol
# p: Last price
# t: UNIX milliseconds timestamp
# v: volume
# c: List of trade conditions. A comprehensive list of trade conditions code can be found at --> https://docs.google.com/spreadsheets/d/1PUxiSWPHSODbaTaoL2Vef6DgU-yFtlRGZf19oBb9Hp0/edit?usp=sharing

# df = pd.DataFrame(columns=['foreignNotional', 'grossValue'])
dfs = []


def on_message(ws, message):
    # df = pd.read_json(message)
    # print(df)
    # print("TEST:" + message + "\n\n\n")

    msg = json.loads(message)
    # dfs.append(pd.DataFrame([msg['data'][0]['p']]))
    #df = pd.concat(dfs, ignore_index=True, sort=False)
    print(msg['data'][0]['p'])

    # print(msg)
    # global df
    # `ignore_index=True` has to be provided, otherwise you'll get
    # "Can only append a Series if ignore_index=True or if the Series has a name" errors
    # df = pd.read_json(msg)
    # print(df)
    # pd.read_json(msg, orient='split')


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0smcq748v6pgu5knkig",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
