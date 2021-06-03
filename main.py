from person import Person, StratB, StratC
from market import Market
from sheets import Sheets
import schedule
import time

# heroku ps:scale worker=1
# heroku ps

m1 = Market('symbols.txt')
p1 = Person(100)
p2 = StratB(100)
p3 = StratC(100)
sheet = Sheets()

def job():
    m1.run()
    p1.run(m1.list_of_stock[0], m1.direction)
    p2.run(m1.list_of_stock[0], m1.direction)
    p3.run(m1.list_of_stock[0], m1.direction)
    # row = [TIME, DIRECTION, CLOSE, MA, CA, MB, CB, MC, CC, ]
    row = [m1.list_of_stock[0].current_time, m1.direction, m1.list_of_stock[0].close_price, p1.get_money(m1.list_of_stock[0].close_price), p1.coin, p2.money, p2.coin, p3.money, p3.coin]
    sheet.add_row(row)
    # p1.display_info()
    # m1.display_info()
    # print(m1.list_of_stock[0].change())
    # print('========================================')

schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)