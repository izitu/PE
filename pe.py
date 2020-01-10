import os
import re
import time

import bs4
import requests
import wget
from selenium import webdriver

s0 = requests.get('http://www.tvc.ru/channel/brand/id/14')
b = bs4.BeautifulSoup(s0.text, "html.parser")

# получаем url и скачиваем картинку
p_url_img = b.select('.series__img-wrap')
string = p_url_img[0]

fnd_src = r'src="(.+?)"'  # поиск src в строке
fnd_sosrc = 'source src="(.+?)"'  # поиск sourse src в строке
fnd_href = r'href="(.+?)"'  # поиск href в строке

ser_img = re.findall(fnd_src, str(string))
print(ser_img[0])
filename = wget.download(ser_img[0])
os.rename(filename, u'' + os.getcwd() + '/' + filename)

# Вынимаем название серии и дату
p_tit = b.select('.series__item .series__item-title')
ser_title = p_tit[0].getText()
p_dat = b.select('.series__month-day .series__item-month')
ser_dat = p_dat[0].getText()
print('Последняя серия :' + ser_title + '  дата:' + ser_dat)
print("--------")

# получаем адрес серии
p_block = b.select('.series__link-block')

string = p_block[0]
result = re.findall(fnd_href, str(string))
print(result[0])

# скачиваем
s1 = requests.get('http://www.tvc.ru' + result[0])
p = bs4.BeautifulSoup(s1.text, "html.parser")

# получаем анонс
p_anons = p.select('.brand__anons-text')
ser_anons = p_anons[0].getText()
print('Анонс: \n для ют. Православная энциклопедия ТВЦ \n для фб. #Православная_энциклопедия\n' + ser_anons)
p_player = p.select('.brand__player-inner')

result = re.findall(fnd_src, str(p_player))
print(result[0])
print('http://www.tvc.ru' + result[0])

driver = webdriver.Firefox()
driver.get('http://www.tvc.ru' + result[0])
time.sleep(5)
htmlSource = driver.page_source
# print(htmlSource)
driver.close()

ser_vid = re.findall(fnd_sosrc, str(htmlSource))
print(ser_vid[0])
print('Скачиваем!!!!')
filename = wget.download(ser_vid[0])
os.rename(filename, u'' + os.getcwd() + '/' + filename)
print("Готово!")
my_file = open("PE.txt", "w")
my_file.write(ser_title)
my_file.write(ser_dat)
my_file.write(
    '\nАнонс: \n для ют. Православная энциклопедия ТВЦ \n для фб. #Православная_энциклопедия\n' + ser_anons + '\n')
my_file.write(ser_img[0] + '\n')
my_file.write(ser_vid[0])

my_file.close()
