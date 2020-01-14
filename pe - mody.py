#
import requests, bs4
import re
import wget, os
import json
from urllib.request import urlopen
#from selenium import webdriver
import time
#series__link-block
s0=requests.get('http://www.tvc.ru/channel/brand/id/14')
b=bs4.BeautifulSoup(s0.text, "html.parser")

# получаем url и скачиваем картинку
if b.find('meta', property='og:video') is not None:
    ser_title = b.find('meta', property='og:title').get('content')
    print(ser_title)

    ser_anons = b.find('meta', property='og:description').get('content')
    print(ser_anons)

    img_url = b.find('meta', property='og:image').get('content')
    print(img_url)

    video_url_raw = b.find('meta', property='og:video').get('content').replace('iframe','json')
    print(video_url_raw)
else:
    print('Ничего не выйдет! - это не первая и единственная серия в году')
    # ищем последнюю серию
    url_last_ser = 'http://www.tvc.ru' + b.find(class_='series__link-block').get('href')
    print(url_last_ser)

    s1 = requests.get(url_last_ser)
    b = bs4.BeautifulSoup(s1.text, "html.parser")

    ser_title = b.find('meta', property='og:title').get('content')
    print(ser_title)

    ser_anons = b.find('meta', property='og:description').get('content')
    print(ser_anons)

    img_url = b.find('meta', property='og:image').get('content')
    print(img_url)

    video_url_raw = b.find('meta', property='og:video').get('content').replace('iframe','json')
    print(video_url_raw)

    #exit(0)
# качаем картинку
filename = wget.download(img_url)
os.rename(filename, u''+os.getcwd()+'/'+filename)

# Вынимаем название серии и дату

dat_raw = b.select('.article__day')
# первый элемент - день недели - берем только текст и удаляем справа все не нужное (перевод стороки)
# плюс пробел
# второй элемент - удаляем повторяющиеся пробелы из текста
ser_dat = dat_raw[0].getText().rstrip() + ' ' + " ".join(dat_raw[1].getText().split())
print (ser_dat)

# Переходим на json ссылку и вынимаем прямой урл
s1=requests.get(video_url_raw).json()
video_url = s1['path']['quality'][0]['url']

print('Скачиваем!!!!')
filename = wget.download(video_url)
os.rename(filename, u''+os.getcwd()+'/'+filename)
print("Готово!")
my_file = open("PE.txt", "w")
my_file.write(ser_title)
my_file.write(ser_dat)
my_file.write('\nАнонс: \n для ют. Православная энциклопедия ТВЦ \n для фб. #Православная_энциклопедия\n' + ser_anons+'\n')
my_file.write(img_url+'\n')
my_file.write(video_url)

my_file.close()
