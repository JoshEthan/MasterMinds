from stock import Stock


class Market:
    def __init__(self, symbols_file):
        self.symbols_file = symbols_file
        self.direction = None
        self.list_of_stock = []
        self.up = 0
        self.down = 0
        self.get_list_of_symbols()
        self.get_list_of_stocks()

    def run(self):
        self.update_stocks()
        self.get_direction()

    def get_list_of_symbols(self):
        f = open(self.symbols_file, "r")
        self.symbols = f.read().splitlines()
        f.close()
    
    def get_list_of_stocks(self):
        for symbol in self.symbols:
            new_stock = Stock(symbol)
            self.list_of_stock.append(new_stock)

    def get_direction(self):
        self.get_percentage()
        if self.up == 100:
            self.direction = 'up'
        elif self.down == 100:
            self.direction = 'down'
        else:
            self.direction = 'neither'
        
    def get_percentage(self):
        self.up = 0
        self.down = 0
        for stocks in self.list_of_stock:
            if stocks.change() > 0:
                self.up += 1
            elif stocks.change() < 0:
                self.down += 1
            else:
                self.up += 0
        self.up = (self.up/len(self.list_of_stock)) * 100
        self.down = (self.down/len(self.list_of_stock)) * 100

    def update_stocks(self):
        for stocks in self.list_of_stock:
            stocks.update()

    def display_info(self):
        print('Symbol File: {}'.format(self.symbols_file))
        print('Direction: {}'.format(self.direction))
        for x in range(len(self.list_of_stock)):
            self.list_of_stock[x].display_info()
        print('Up: {}'.format(self.up))
        print('Down: {}'.format(self.down))