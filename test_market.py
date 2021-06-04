import unittest
from market import Market
import time


class TestMarket(unittest.TestCase):
    m1 = Market('symbols.txt')

    def test_list_of_symbols(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.get_list_of_symbols()
        print(self.m1.symbols)

    def test_list_of_stocks(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.get_list_of_symbols()
        self.m1.get_list_of_stocks()
        print(self.m1.list_of_stock[0].symbol)

    def test_stock_mark_price(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.get_list_of_symbols()
        self.m1.get_list_of_stocks()
        print(self.m1.list_of_stock[0].market_price)

    def test_stock_price_change(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        # self.m1.get_list_of_symbols()
        # self.m1.get_list_of_stocks()
        # # print(self.m1.list_of_stock[0].change())
        # # print(self.m1.list_of_stock[0].change())
        # print('TESTING')

    def test_stock_price_change_V2(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.run()
        self.m1.run()
        self.m1.run()
        print('{:f}'.format(self.m1.list_of_stock[0].change()))

    def test_stock_price_change(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.get_list_of_symbols()
        self.m1.get_list_of_stocks()
        self.m1.get_direction()
        print(self.m1.up)
        print(self.m1.down)
        print(self.m1.direction)

    def test_final_return(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.get_list_of_symbols()
        self.m1.get_list_of_stocks()
        self.m1.get_direction()
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].get_close_price())
        print()
        time.sleep(5)
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].get_close_price())
        print(self.m1.list_of_stock[0].current_time)
        print()
        time.sleep(5)
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].get_close_price())

    def test_final_return_v2(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.run()
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].get_close_price())
        print()
        time.sleep(5)
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].get_close_price())
        print(self.m1.list_of_stock[0].current_time)
        print()
        time.sleep(5)
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].get_close_price())

    def test_final_return_v3(self):
        self.m1.symbols_file = "C:/git/MasterMinds/symbols.txt"
        self.m1.run()
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].close_price)
        self.m1.list_of_stock[0].change()
        print()
        time.sleep(5)
        self.m1.run()
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].close_price)
        print(self.m1.list_of_stock[0].current_time)
        print()
        time.sleep(5)
        self.m1.run()
        print(self.m1.direction)
        print(self.m1.list_of_stock[0].open_price)
        print(self.m1.list_of_stock[0].close_price)