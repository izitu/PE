import requests, bs4
import re
import wget, os
import json
from urllib.request import urlopen
import time

ser_num = 2

s0=requests.get('http://www.tvc.ru/channel/brand/id/14')
b0=bs4.BeautifulSoup(s0.text, "html.parser")

# собираем все блоки html с сериями
ser_all_block = b0.find_all(class_='series__link-block')

# выводим все ссылки с сериями
num = 1
for ser in ser_all_block:
    # смотрим только нужное количество серий
    if num > ser_num:
        break
    # print(ser)

    # вынимаем дату серии
    ser_date = ser.find(class_='series__item-month').text
    # удаляем лишние пробелы
    ser_date = " ".join(ser_date.split())
    print(ser_date)

    # вынимаем заголовок
    ser_title = ser.find(class_='series__item-title').text
    # удаляем лишние пробелы
    ser_title = " ".join(ser_title.split())
    ser_title = ser_title.replace('"', '')
    print(ser_title)

    url = 'http://www.tvc.ru' + ser.get('href')
    print(url)

    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, "html.parser")

    # ser_title = b.find('meta', property='og:title').get('content')
    # print(ser_title)

    ser_anons = b.find('meta', property='og:description').get('content')
    print(ser_anons)

    img_url = b.find('meta', property='og:image').get('content')
    print(img_url)

    video_url_raw = b.find('meta', property='og:video').get('content').replace('iframe','json')
    print(video_url_raw)

    # Переходим на json ссылку и вынимаем прямой урл
    sv = requests.get(video_url_raw).json()
    video_url = sv['path']['quality'][0]['url']

    print('Скачиваем!!!!')
    wget.download(img_url)
    wget.download(video_url)

    my_file = open(f"P{num}.txt", "w")
    
    my_file.writelines(ser_date + '\n')
    my_file.writelines('*' * 15 + '\n')
    my_file.writelines(ser_title + '\n')
    my_file.writelines('*' * 15 + '\n')
    my_file.writelines(ser_anons + '\n')
    my_file.writelines('*' * 15 + '\n')
    my_file.writelines(img_url + '\n')
    my_file.writelines(video_url + '\n')
    my_file.writelines('Православная энциклопедия ТВЦ')

    my_file.close()

    num = num + 1

print("Готово!")
#print(b)