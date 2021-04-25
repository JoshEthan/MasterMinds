"""
This is a comment
written in
more than just one line
"""
import websocket
import pandas as pd
import json
import schedule
import time
import os
from os import system
import os.path
from os import path

"""
Global Variables: This is a list of global variables 
    that will be initiated here then used throughout the program.
"""
df = pd.DataFrame({'Close': []})
close = 0
stock_dic = {}
START_TICKER = 51
END_TICKER = 100

"""
Job Function: This is called by the schedule function every X seconds. This will take all the data 
    aquired and then store it into a directory. It stores what ever information is on the stock_dic.
"""
def job():
    global df
    for key in stock_dic:
        if (path.exists('tickerPrices//' + key)):
            df = pd.read_csv('tickerPrices//' + key)
        else:
            df = pd.DataFrame({'Close': []})
        df = pd.concat(
            [df, pd.DataFrame({'Close': [stock_dic[key]]})], ignore_index=True)
        df.to_csv('tickerPrices//' + key, index=False)
    print('*****Data added to files.*****')

"""
Web Socket Function: This function pulls the actual information. We wait 5 seconds then clear the terminal.
    After that we start to pull information and display it.
"""
def on_message(ws, message):
    time.sleep(2)
    system('cls')
    print('Getting data...')
    msg = json.loads(message) # This is all the information (too much information)
    global close
    #print(msg)
    close = msg['data'][0]['p'] # This is the important information
    schedule.run_pending() # WHAT?
    time.sleep(1) # WHAT?
    print('Data aquired.')
    #print(msg['data'][0])
    #print('Adding data to dictionary...')
    i = START_TICKER
    file = open('Tickers.txt', 'r') # Opens the file
    for data in msg['data']:
        while i < END_TICKER: # To Loop through our list of tickers
            ticker = file.readline()
            i += 1
            #print(data)
            if data['s'] == ticker.strip():
                    stock_dic[ticker.strip()] = data['p']
    print(stock_dic)
    file.close()

"""
Web Socket Function: This function prints an error statement when there is an error.
"""
def on_error(ws, error):
    print(error)

"""
Web Socket Function: This function prints a statement when the web socket is closed.
"""
def on_close(ws):
    print("### closed ###")

"""
Web Socket Function: This function is called when the web socket is being opened.
    It can only pull 50 stocks at a time. This is the function to specify which tickers
    it is currently pulling. It will use the 'Tickers.txt' file and pull those names.
"""
def on_open(ws):
    system('cls') # This should clear the terminal
    file = open('Tickers.txt', 'r') # Opens the file
    print('Opening stocks...')
    i = START_TICKER
    while True: # To Loop through our list of tickers
        ticker = file.readline()
        #print('Opened: ' + ticker.strip()) # Shows which tickers have been opened.
        ws.send('{"type":"subscribe","symbol":"' + ticker.strip() + '"}') # Opens the stock info
        i += 1
        if i == END_TICKER: # Loops ends when it reaches max
            break
    file.close()

schedule.every(10).seconds.do(job)  # Add data to csv every X seconds

"""
Web Socket Loop: This function allows the web socket to run 
    forever until the user inputs 'ctrl-c' into the terminal.
"""
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0smcq748v6pgu5knkig",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()