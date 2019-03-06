from sheet import *

#kita tentukan file mana yang mau kita gunakan
wks = gc.open("customerEmail")

#memakai worksheet bernama data User
sh1 = wks.worksheet("Sheet1")

#meneukan value pada KOLOM parameter adalah Nomer KOLOM
colUsername =  sh1.col_values(1)
colPassword = sh1.col_values(3)

#menemukan row values
rw = sh1.row_values(2)

#meneumak string tertentu pada all sheet
fd = sh1.find("aprilianisah.91@gmail.com")

print(f"di temukan pada Row : {fd.row} dan Column : {fd.col}")



