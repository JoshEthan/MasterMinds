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

TOTAL_STOCKS = 0
directory = 'tickerPrices' # Name of the directory with the prices

"""
Display: Function simplifies the display in the terminal.
"""
def print_DF(df):
    print_seperators()
    print("NAME OF DATABASE: ")
    print("----------------------------------------")
    print(df)
    print_seperators()

"""
Display: Function simplifies the display in the terminal.
"""
def print_seperators():
    print("\n\n\n")


def clear(): return system('cls')

"""
Display: Function that displays the current market time.
"""
def print_time():
    market_tz = pytz.timezone('US/Eastern')
    market_datetime = datetime.now(market_tz)
    print("Market time:", market_datetime.strftime("%H:%M:%S"))


"""
Calculation: Function returns the percentage.
"""
def get_percentage_total(num_stocks):
    percentage = (num_stocks/TOTAL_STOCKS) * 100
    # DEBUG
    # print(num_stocks)
    # print(TOTAL_STOCKS)
    # print(percentage)
    return round(percentage, 2)

# WHat is this for?
empty = 0

"""
Gather Info: This function will open 'tickerPrice' directory and store that info.
    Loops through directory, gets the stock name and the percentage change.
"""
def get_all_stocks():
    #print_time()
    all_df = pd.DataFrame({'Tick': [], 'Percentage': []})
    global empty
    global TOTAL_STOCKS
    #print("Getting all stocks...\n")
    for filename in os.listdir(directory):
        # print(filename) # Show us what stock we are on
        stock_name = (filename).split('.')[0]
        data = pd.read_csv(directory+'//'+filename, delimiter=",")
        percentage = round(data['Close'].tail(
            2).pct_change() * 100, 2)[len(data)-1]
        new_stock = pd.DataFrame(
            {'Tick': [stock_name], 'Percentage': [percentage]})
        all_df = pd.concat([all_df, new_stock], ignore_index=True)
        TOTAL_STOCKS += 1 # To find TOTAL_STOCKS
    print("TOTAL STOCKS:" + str(TOTAL_STOCKS)) # DEBUG
    return all_df

"""
Job: Scheduled to run every X seconds. Store a list of all the tickers and their change in percentage
    into a DF. Take that DF and ...
"""
def job():
    #print_time()
    #print("Started job...\n")
    clear()
    all_df = get_all_stocks()
    market_totals = get_total_up_and_down(all_df)
    get_market_percentages(
        market_total_up=market_totals[0], market_total_down=market_totals[1])

"""
Get Totals: Get the # of positive and negative percentages.
"""
def get_total_up_and_down(all_df):
    #print_time()
    #print("Getting Total Up and Down...\n")
    market_total_up = 0
    market_total_down = 0
    for index, row in all_df.iterrows():
        if row['Percentage'] > 0:
            market_total_up += 1
        else:
            market_total_down += 1
    # DEBUG
    #print(market_total_up)
    #print(market_total_down)
    return [market_total_up, market_total_down]

"""
Market Percentage: This is the function that prints out the negative and positive
    percentages.
"""
def get_market_percentages(market_total_up, market_total_down):
    market_up_percentage = get_percentage_total(market_total_up)
    market_down_percentage = get_percentage_total(market_total_down)
    global TOTAL_STOCKS
    TOTAL_STOCKS = 0
    #clear()
    print("MARKET PERCENTAGES: ")
    print_time()
    print("---------------------")
    print("+{0}%   -{1}%".format(market_up_percentage, market_down_percentage))
    #print_seperators()

schedule.every(10).seconds.do(job)  # For the small directory

while True:
    # Use these for the smaller directory
    schedule.run_pending()
    time.sleep(1)
    # job() # It takes about 40sec to read all the data, use this when using Stocks directory
