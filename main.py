from datetime import datetime

#1.Создайте словарь email
email = {
"subject": " Weekd plans ",
    "from": "katya_yan@yandex. ",
    "to": "frid@mail. ",
    "body": "\tHey!\nLet's go hiking this weekd.\nBring snacks!\n"
}

print(email)

#2. Добавьте дату отправки
send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date
print(send_date)

