import json
import time
import schedule
import threading
import websocket
import pandas as pd
from os import system
from datetime import datetime
import pytz
import os

# PULLS DATA FROM TEXT FILES, WORKS PRETTY GOOD. DON'T THINK I NEED TO CHANGE THIS ONE AT ALL. KEEP
# AN EYE OUT FOR THE DIRECTORY YOU USE AND THE SCHEDULING.

TOTAL_STOCKS = 1  # 7163 for large directory
directory = 'oneMinStocks'  # OR 'Stocks'


def print_DF(df):
    print_seperators()
    print("NAME OF DATABASE: ")
    print("----------------------------------------")
    print(df)
    print_seperators()


def print_seperators():
    print("\n\n\n")


# Clear terminal


def clear(): return system('cls')

# Return total percentage


def get_percentage_total(num_stocks):
    percentage = (num_stocks/TOTAL_STOCKS) * 100
    # DEBUG
    # print(num_stocks)
    # print(TOTAL_STOCKS)
    # print(percentage)
    return round(percentage, 2)


empty = 0
num_files = 0


def get_all_stocks():
    print_time()
    all_df = pd.DataFrame({'Tick': [], 'Percentage': []})
    global empty
    print("Getting all stocks...\n")
    for filename in os.listdir(directory):
        # print(filename) # Show us what stock we are on
        stock_name = (filename).split('.')[0]
        if os.stat(directory+'//'+filename).st_size == 0:
            # print("EMPTY FILE")
            empty += 1
        else:
            data = pd.read_csv(directory+'//'+filename, delimiter=",")
            percentage = round(data['Close'].tail(
                2).pct_change() * 100, 2)[len(data)-1]
            new_stock = pd.DataFrame(
                {'Tick': [stock_name], 'Percentage': [percentage]})
            all_df = pd.concat([all_df, new_stock], ignore_index=True)
    return all_df
    # num_files += 1 # To find TOTAL_STOCKS
    # print(num_files) # DEBUG


# apple_data = {'Time': ['9:30AM', '10:00AM'], 'Previous Price': [
#     119.90, 121.63], 'Current Price': [121.63, 123.02], 'Percentage': ["+1.4%", "+1.1%"]}
# apple_df = pd.DataFrame(data=apple_data)
# print_DF(apple_df)

# all_data = {'Tick': [
#     "APPL", "TSLA", "BAC", "MSFT", "AMZN", "GOOG", "GOOGL", "FB", "BABA", "TSM"], 'Percentage': [1.4, -1.1, -0.8, 1.7, 1.3, 0.6, 0.8, 2.3, -1.1, 2.8]}
# all_df = pd.DataFrame(data=all_data)
# --Print list of stocks with their percentages
# print_DF(all_df)

# Will iterate through the list of stocks and count the UPs and the DOWNs
#   then return a list

def job():
    print_time()
    print("Started job...\n")
    all_df = get_all_stocks()
    market_totals = get_total_up_and_down(all_df)
    get_market_percentages(
        market_total_up=market_totals[0], market_total_down=market_totals[1])


def get_total_up_and_down(all_df):
    print_time()
    print("Getting Total Up and Down...\n")
    market_total_up = 0
    market_total_down = 0
    for index, row in all_df.iterrows():
        if row['Percentage'] > 0:
            market_total_up += 1
        else:
            market_total_down += 1
    # DEBUG
    # print(market_total_up)
    # print(market_total_down)
    return [market_total_up, market_total_down]

# Prints out the percentage of total ups and total downs


def get_market_percentages(market_total_up, market_total_down):
    market_up_percentage = get_percentage_total(market_total_up)
    market_down_percentage = get_percentage_total(market_total_down)
    # clear()
    print("MARKET PERCENTAGES: ")
    print_time()
    print("---------------------")
    print("+{0}%   -{1}%".format(market_up_percentage, market_down_percentage))
    print_seperators()

# Gives us current time of the market


def print_time():
    market_tz = pytz.timezone('US/Eastern')
    market_datetime = datetime.now(market_tz)
    print("Market time:", market_datetime.strftime("%H:%M:%S"))


# print("Loading: ", end="")
# schedule.every(1).seconds.do(print, ".", end="", flush=True)
# schedule.every(5).seconds.do(clear)
# schedule.every(5).seconds.do(get_all_stocks)
# market_totals = get_total_up_and_down()  # Get total ups and downs
# schedule.every(5).seconds.do(get_market_percentages,
#                               market_total_up=market_totals[0], market_total_down=market_totals[1])  # Run every 5 sec then print out market ups and down percentages


schedule.every(60).seconds.do(job)  # For the small directory

while True:
    # Use these for the smaller directory
    schedule.run_pending()
    time.sleep(1)
    # job() # It takes about 40sec to read all the data, use this when using Stocks directory
