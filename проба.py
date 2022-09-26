import requests
import datetime

url_nbu = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

try:
    data_from_url_nbu = requests.request('GET', url_nbu)
except Exception as e:
    print(e)
else:
    if 300 > data_from_url_nbu.status_code >= 200:
        if content := data_from_url_nbu.headers.get('Content-Type'):
            if content == 'application/json; charset=utf-8':
                with open('Exchange Rates.txt', 'a', encoding='utf-8') as file:
                    file.write(str(datetime.datetime.now()) + '\n\n')
                    position = 1
                    for currency in data_from_url_nbu.json():
                        file.write(f'{position}. {currency["txt"]} - {currency["rate"]}' + '\n')
                        position += 1