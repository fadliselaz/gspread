# gspread
input data to google spread sheet

# Cara Pakai
ini adalah sedikit tutorial pemakaiannya :

# 1. Memberikan Akses API Sheet
kali ini kita akan konneckan app kita dengan memanfaatkan google sheet sebagai penyimpanana data nya..

Tapi kali ini kita tidak menggunkana GCP yang berbayar,
hanya menggunakan google api gratis dari google devereper..

silakan ke web berikut ini:

https://console.developers.google.com

lalu buat sebuah new project,
setelah itu kita klik DASHBOARD
dan kita klik enable APIS and service 

pertama kita cari google sheet api dulu,
dan aktifkan

lalu kita cari google drive api
lalu kita aktifkan kembali..

setelah itu kita kembali ke dashboard,
lalu kita klik CREDENTIALS

pilih SERVICE ACCOUNT KEYS

pilih NEW,
dan JSON

lalu klik create..

selanjutnya file JSON akan terdownload ke komputer kita..

# 2 Ambil email Credetiao dari JSON
Selanjut silakan kita taruh file JSON tadi ke dalam folder project kita

dan silakan buka.. akan ada file seperti ini :

{
  "type": "service_account",
  "project_id": "praxis-study-233220",
  "private_key_id": "53a708734e3ffc132cdd5f99056012cc827a4ed5",
  "private_key": "-----BEGIN PRIVATE KEY----------END PRIVATE KEY-----\n",
  "client_email": "fadliselaz@praxis-study-233220.iam.gserviceaccount.com",
  "client_id": "106541770825382871298",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/fadliselaz%40praxis-study-233220.iam.gserviceaccount.com"
}

nah 
silakan kalian copy value pada client_email

# 3 Konfigurasi File Sheet
Buat sebuah file di google sheet,
namakan sesuai keingian..

lalu kita klik tombol share,
masukan CLIENT_EMAIL yang kita copy dari file JSON hasil Credential tadi,
pada kolom PEOPLE,

hal ini berarti kita share sheet kita kepada email sheet API,
dengan ini API SHeet bisa mengobrak abrik sheet kita..


