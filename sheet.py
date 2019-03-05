import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('test.json', scope)

#menjadikan variable gc
gc = gspread.authorize(credentials)

# work sheet yang dipakai
wks = gc.open("sheet").sheet1

print(wks.get_all_records())