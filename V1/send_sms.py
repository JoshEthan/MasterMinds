# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC37ecbd268a88d726aa9882f361fad562"
auth_token = "d5968eb0abcbd6cbae880cbd261969fe"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hot off the press! \n 8=====D",
                    from_='+15717770692',
                    to='+14803886978'
                )

print(message.sid)

# To run this code:
#       python send_sms.py
