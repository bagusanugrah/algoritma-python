import re
import requests

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d]).+$'

inputan_benar = False

while not inputan_benar:
    print()
    email = input('email: ')
    password = input('password: ')

    if re.match(email_regex, email) and re.match(password_regex, password):
        inputan_benar = True
    else:
        if not re.match(email_regex, email):
            print('Inputan email salah!')
        
        if not re.match(password_regex, password):
            print('Password harus mengandung huruf besar, huruf kecil, angka, dan simbol!')

url = "http://localhost:8000/data-user"
params = {"email": email, "password": password}

response = requests.post(url, params=params)

if response.status_code == 200:
    print("Berhasil kirim data!")
    print("Response:", response.json())
else:
    print("Gagal kirim data!")
    print("Response:", response.text)