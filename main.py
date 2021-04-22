import json
import time
import schedule
import threading
import websocket
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


# Define needed variables
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
global currentPrice
currentPrice = 0.0


def sendMessage(percentage):
    # client.messages \
    #     .create(
    #         body="Hot off the press! \n 8=====D",
    #         from_='+15717770692',
    #         to='+14803886978'
    #     )
    print("Percentage of Change: " + str(round(percentage, 2)) + "%\n")


def getPercentageChange(previousPrice, currentPrice):
    return ((currentPrice - previousPrice) / previousPrice) * 100

# Function to run after set amount of time


def job():
    previousPrice = 120.78
    print("\nPrevious Price: " + str(previousPrice))
    print("Current Price: " + str(currentPrice))
    sendMessage(getPercentageChange(previousPrice, currentPrice))
    previousPrice = currentPrice

# Functions for web socket


def getPrice():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0smcq748v6pgu5knkig",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    wst = threading.Thread(target=ws.run_forever)
    wst.start()
    time.sleep(30)
    print(currentPrice)
    time.sleep(30)
    print(currentPrice)
    time.sleep(30)
    print(currentPrice)
    time.sleep(30)
    print(currentPrice)
    ws.keep_running = False
    wst.join()
    job()


def on_message(ws, message):
    msg = json.loads(message)
    global currentPrice
    if msg['data'][0]['p'] != None:
        currentPrice = msg['data'][0]['p']
    else:
        currentPrice = 1


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')


# Runs every alloted time
schedule.every(5).seconds.do(job)


if __name__ == "__main__":
    getPrice()
    # Continuosly run
    # while True:
    #   schedule.run_pending()
    #  time.sleep(1)


# type: Message Type
# data: List of trades or price updates
# s: Symbol
# p: Last price
# t: UNIX milliseconds timestamp
# v: volume
# c: List of trade conditions. A comprehensive list of trade conditions code can be found at --> https://docs.google.com/spreadsheets/d/1PUxiSWPHSODbaTaoL2Vef6DgU-yFtlRGZf19oBb9Hp0/edit?usp=sharing


# TODO: 1. Continuosly run Websocket on another thread
#       2. Every 5min grab the current price
#       3. Find rate of change
#       4. If RoC is >= 10% send message
#       5. Set oldPrice = currentPrice
#       6. Repeat 2-5
