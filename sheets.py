import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Sheets:
    def __init__(self):
        self.scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Robinhood Data").sheet1

    def add_row(self, row):
        self.sheet.insert_row(row, 2)

# data = sheet.get_all_records()

# row = sheet.row_values(3)
# col = sheet.col_values(3)
# cell = sheet.cell(1, 2).value

# insertRow = ['hello', 5, 'red', 'blue']
# sheet.insert_row(row, 4)
# sheet.delete_rows(4)
# sheet.update_cell(2, 2, "CHANGED")

# for x in range(30):
#     quote = r.crypto.get_crypto_quote('DOGE')
#     q = float(quote['mark_price'])

#     # pprint(row)
#     # pprint(col)
#     # ['2', 'Bill', 'blue']
#     # pprint([q, 'Bill', 'blue'])
#     sheet.insert_row([q], 4)

    # pprint(row)
    # pprint(col)
    # ['2', 'Bill', 'blue']
    # pprint([q, 'Bill', 'blue'])
    # sheet.insert_row([q], 2)