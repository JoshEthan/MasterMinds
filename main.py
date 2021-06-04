from person import Person, StratB, StratC, StratD
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
p4 = StratD(100)
sheet = Sheets()

def job():
    m1.run()
    p1.run(m1.list_of_stock[0], m1.direction)
    p2.run(m1.list_of_stock[0], m1.direction)
    p3.run(m1.list_of_stock[0], m1.direction)
    p4.run(m1.list_of_stock[0], m1.direction)
    # row = [TIME, DIRECTION, CLOSE, MA, CA, MB, CB, DB, MC, CC, DC]
    row = [m1.list_of_stock[0].current_time, m1.direction, m1.list_of_stock[0].close_price, 
        p1.get_money(m1.list_of_stock[0].close_price), p1.coin,
        p2.money, p2.coin, p2.get_price_difference(), 
        p3.money, p3.coin, p3.get_price_difference(),
        p4.money, p4.coin, p4.get_price_difference()]
    sheet.add_row(row)
    move = 0
    if p3.hasReset:
        move += 3
    sheet.add_to_sheet2(p2.buyCounter, p3.buyCounter, p4.buyCounter, move)
    # p1.display_info()
    # m1.display_info()
    # print(m1.list_of_stock[0].change())
    # print('========================================')

schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)