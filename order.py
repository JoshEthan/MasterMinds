class Order:
    def __init__(self):
        self.buy_price = 0
    
    def change(self, close):
        if self.buy_price != 0:
            change = (close - self.buy_price)/abs(self.buy_price)
            return change
        else:
            return 0
