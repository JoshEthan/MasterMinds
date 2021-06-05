from datetime import datetime, timedelta

class Person:
    def __init__(self, money):
        self.money = money
        self.coin = 0
        self.action = '-'
        self.price_diff = ''
        self.stock = None
        self.direction = None
        self.initial_buy = 0
        self.buyCounter = 0
        # self.reset = 0
        # self.day = 3
        # self.hasReset = False

    def run(self, stock, direction):
        self.stock = stock
        self.direction = direction
        self.set_action()
        self.check_action()
        self.initial_buy_in()
        # self.update_time()
        
    def check_action(self):
        if self.action == 'B':
            self.price_diff = '{:f}'.format(self.stock.change())
        elif self.action == 'S':
            self.price_diff = '{:f}'.format(self.stock.change())
        else:
            self.price_diff = ''

    def set_action(self):
        if self.direction == 'up' and self.money:
            self.buy(self.stock.close_price)

    def initial_buy_in(self):
        if self.initial_buy == 0:
            self.buy()
            self.initial_buy = self.stock.close_price

    def buy(self, close):
        self.action = 'B'
        self.coin = self.money / close
        self.money = 0
        self.buyCounter += 1
        if self.initial_buy == 0:
            self.initial_buy = close
        if self.reset == 0:
            self.reset = datetime.now()

    def sell(self, close):
        self.money = self.coin * close
        self.coin = 0
        self.action = 'S'
    
    def get_money(self, close):
        if self.money == 0:
            return self.coin * close
        else:
            return self.money

    def get_price_difference(self):
        if self.action == '-':
            return ''
        else:
            diff = ('{}: {}'.format(self.action, self.price_diff))
            self.action = '-'
            return diff

    def display_info(self):
        print('Amount of money: ${}'.format(self.money))
        print('Amount of coin: ${}'.format(self.coin))

    # def update_time(self):
    #     if self.reset != 0:
    #         if self.reset == datetime(2021, 6, self.day):
    #             self.buyCounter = 0
    #             self.reset = self.stock.current_time
    #             self.day += 1
    #             self.hasReset = True
    #         else:
    #             self.hasReset = False

class StratB(Person):
    def __init__(self, money):
        super().__init__(money)

    def set_action(self):
        if self.direction == 'up' and self.money > 0:
            self.buy(self.stock.close_price)
        elif self.direction == 'down' and self.coin > 0:
            self.sell(self.stock.close_price)
        else:
            pass

class StratC(Person):
    def __init__(self, money):
        super().__init__(money)

    def set_action(self):
        if self.stock.change() > 0 and self.money > 0:
            self.buy(self.stock.close_price)
        elif self.direction == 'down' and self.coin > 0:
            self.sell(self.stock.close_price)
        else:
            pass

class StratD(Person):
    def __init__(self, money):
        super().__init__(money)

    def set_action(self):
        if self.stock.change() > self.stock.close_price * 0.003 and self.money > 0:
            self.buy(self.stock.close_price)
        elif self.direction == 'down' and self.coin > 0:
            self.sell(self.stock.close_price)
        else:
            pass

class StratE(Person):
    def __init__(self, money):
        super().__init__(money)

    def set_action(self):
        if self.stock.change() > self.stock.close_price * 0.003 and self.money > 0:
            self.buy(self.stock.close_price)
        elif self.direction == 'down' and self.coin > 0 and self.stock.change() < self.stock.close_price * 0.003:
            self.sell(self.stock.close_price)
        else:
            pass
