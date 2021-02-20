from config import CONSUMER_KEY, REDIRECT_URL, JSON_PATH
from td.client import TDClient

# Create a new instance of the client
td_client = TDClient(client_id=CONSUMER_KEY,
                     redirect_uri=REDIRECT_URL, credentials_path=JSON_PATH)

td_client.login()
