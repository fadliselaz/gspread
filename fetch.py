from sheet import *
import time
import random



#kita tentukan file mana yang mau kita gunakan
wks = gc.open("customerEmail")

#memakai worksheet bernama data User
sh1 = wks.worksheet("Sheet1")

#meneukan value pada KOLOM parameter adalah Nomer KOLOM
colUsername =  sh1.col_values(1)
colPassword = sh1.col_values(3)

#menemukan row values
rw = sh1.col_values(2)
rwl = len(rw)

#meneumak string tertentu pada all sheet
#fd = sh1.find("aprilianisah.91@gmail.com")
nm = [1,2,3,4,5]
rnm = random.choice(nm)

for i in range(rwl):
	print("Whatsapp sent to : " + rw[i])
	time.sleep(rnm)





