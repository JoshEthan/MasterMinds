import robin_stocks.robinhood as r
import pyotp
from config import USERNAME, PASSWORD, KEY
from datetime import datetime, timedelta
from pytz import timezone



totp  = pyotp.TOTP(KEY).now()
login = r.login(USERNAME,PASSWORD, mfa_code=totp)

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.quote = r.crypto.get_crypto_quote(self.symbol)
        self.open_price = float(self.quote['mark_price'])
        self.close_price = float(self.quote['mark_price'])
        self.current_time = self.get_current_time()
        self.SMA = None
        self.close_price_list = []
        self.list_size = 20
        # Have close and open initialize as the same
        # Maybe only open price initializes
        # get close price will set open price to it
        # get mark price exists???
        # Maybe only close and only open
        # getting close will set open to a new number

    def update(self):
        self.open_price = self.close_price
        self.close_price = float(r.crypto.get_crypto_quote(self.symbol)['mark_price'])
        self.current_time = self.get_current_time()
        self.update_close_price_list()
        self.get_SMA()

    def change(self):
        change = (self.close_price - self.open_price)   # / self.open_price
        return change

    def get_SMA(self):
        if len(self.close_price_list) == self.list_size:
            self.SMA = sum(self.close_price_list)/len(self.close_price_list)
        else:
            self.SMA = None

    def update_close_price_list(self):
        if len(self.close_price_list) == self.list_size:
            self.close_price_list.pop(0)
            self.close_price_list.append(self.close_price)
        else:
            self.close_price_list.append(self.close_price)

    # def get_close_price(self):
    #     self.close_price = float(r.crypto.get_crypto_quote(self.symbol)['mark_price'])
    #     self.current_time = self.get_current_time()
    #     return self.close_price

    def get_current_time(self):
        datetime_obj = datetime.now().replace(tzinfo=timezone('US/Arizona'))
        return datetime_obj.strftime("%H:%M:%S\n%m/%d/%Y")
    
    def display_info(self):
        print('\tSymbol: {}'.format(self.symbol))
        print('\tPrice: {}'.format(self.open_price))
        print('\tTime: {}'.format(self.current_time))