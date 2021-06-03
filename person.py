class Person:
    def __init__(self, money):
        self.money = money
        self.coin = 0
        self.canBuy = True

    def run(self, stock, direction):
        if direction == 'up' and self.money:
            self.buy(stock.close_price)

    def buy(self, close):
        self.coin = self.money / close
        self.money = 0

    def sell(self, close):
        self.money = self.coin * close
        self.coin = 0
    
    def get_money(self, close):
        if self.money == 0:
            return self.coin * close
        else:
            return self.money

    def display_info(self):
        print('Amount of money: ${}'.format(self.money))
        print('Amount of coin: ${}'.format(self.coin))

class StratB(Person):
    def __init__(self, money):
        super().__init__(money)

    def run(self, stock, direction):
        if direction == 'up' and self.money:
            self.buy(stock.close_price)
        elif direction == 'down' and self.coin:
            self.sell(stock.close_price)
        else:
            pass

class StratC(Person):
    def __init__(self, money):
        super().__init__(money)

    def run(self, stock, direction):
        if stock.change() > 0 and self.money:
            self.buy(stock.close_price)
        elif direction == 'down' and self.coin:
            self.sell(stock.close_price)
        else:
            pass