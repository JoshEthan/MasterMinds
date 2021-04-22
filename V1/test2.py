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
global previousPrice
previousPrice = 0.1


def getPercentageChange(previousPrice, currentPrice):
    return ((currentPrice - previousPrice) / previousPrice) * 100


def test():
    global previousPrice
    print("The Current Price: ", currentPrice)
    print("The Previous Price", previousPrice)
    print("The percentage change: ", str(
        round(getPercentageChange(previousPrice, currentPrice), 2)) + '%\n')
    previousPrice = currentPrice

# def sched_job():
#     return schedule.CancelJob

# schedule.every().day.at('13:56').do(sched_job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


def sendMessage():
    time.sleep(2)
    print("This is the sendMessage function.")
    schedule.every(60).seconds.do(test)  # Runs every x seconds
    # while True:

    t_end = time.time() + 300  # What does this do again? x sec from right now
    while time.time() < t_end:  # Run for x seconds
        schedule.run_pending()
        time.sleep(1)


def getPrice():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0smcq748v6pgu5knkig",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    messageThread = threading.Thread(target=sendMessage)
    websocketThread = threading.Thread(target=ws.run_forever)
    websocketThread.start()
    time.sleep(2)
    print("\nWait 10 seconds then close.")
    messageThread.start()
    time.sleep(300)  # Time that the web socket will stay open
    ws.keep_running = False
    messageThread.join()
    websocketThread.join()
    print("Joined the web socket and message thread. \n")


def on_message(ws, message):
    msg = json.loads(message)
    global currentPrice
    currentPrice = msg['data'][0]['p']


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"CLVS"}')


if __name__ == "__main__":
    getPrice()
    #messageThread = threading.Thread(target=job)
    # messageThread.join()
