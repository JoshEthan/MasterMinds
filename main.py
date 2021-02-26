import schedule
import time
from twilio.rest import Client
from alpha_vantage.timeseries import TimeSeries

API_KEY = "VEBHU4J9S5T4AR81"
account_sid = "AC37ecbd268a88d726aa9882f361fad562"
auth_token = "d5968eb0abcbd6cbae880cbd261969fe"
client = Client(account_sid, auth_token)
# Aplha Vantage: VEBHU4J9S5T4AR81

ts = TimeSeries(key=API_KEY, output_format='pandas')
data = ts.get_daily_adjusted('AAPL')


def job():
    client.messages \
        .create(
            body="Hot off the press! \n 8=====D",
            from_='+15717770692',
            to='+14803886978'
        )
    print('Message Sent.')


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
