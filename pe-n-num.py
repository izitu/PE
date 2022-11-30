import os
import re
import time

import bs4
import requests
import wget
from selenium import webdriver

s0 = requests.get('http://www.tvc.ru/channel/brand/id/14')
b = bs4.BeautifulSoup(s0.text, "html.parser")
print("Введите количество последних серий, которые хотите скачать:")
ser_num = int(input())
# ser_num = 2  # количество скачиваемых серий
# ser_num = ser_num 22- 1

fnd_src = r'src="(.+?)"'  # поиск src в строке
fnd_sosrc = 'source src="(.+?)"'  # поиск sourse src в строке
fnd_href = r'href="(.+?)"'  # поиск href в строке

# получаем url и скачиваем картинку
p_url_img = b.select('.series__img-wrap')
string = p_url_img[0]
print(p_url_img)
ser_img = re.findall(fnd_src, str(p_url_img))

# Вынимаем название серии и дату
p_tit = b.select('.series__item .series__item-title')
p_dat = b.select('.series__month-day .series__item-month')
# получаем адрес серии
p_block = b.select('.series__link-block')
print (ser_num)


for ser in reversed(range(ser_num)):
	print(ser, ser_img[ser])
	filename = wget.download(ser_img[ser])
	os.rename(filename, u'' + os.getcwd() + '/' + filename)

	ser_title = p_tit[ser].getText()
	ser_dat = p_dat[ser].getText()
	print('Серия: ' + str(ser) + ' ' + ser_title + '  дата:' + ser_dat)
	result = re.findall(fnd_href, str(p_block[ser]))
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

	# fp = webdriver.FirefoxProfile()
	# fp.set_preference('app.update.auto', False)
	# fp.set_preference('app.update.enabled', False)
	# driver = webdriver.Firefox(firefox_profile=fp)
	driver = webdriver.Firefox()

	# driver = webdriver.Firefox()
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
	namefil = "PE" + str(ser) + ".txt"
	my_file = open(namefil, "w")
	my_file.write(ser_title)
	my_file.write(ser_dat)
	my_file.write(
		'\nАнонс: \n для ют. Православная энциклопедия ТВЦ \n для фб. #Православная_энциклопедия\n' + ser_anons + '\n')
	my_file.write(ser_img[ser] + '\n')
	my_file.write(ser_vid[0])

	my_file.close()

exit(0)
print(p_block)

string = p_block[0]
print(p_block)
result = re.findall(fnd_href, str(string))
print(result)
exit(0)
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
# filename = wget.download(ser_vid[0])
# os.rename(filename, u''+os.getcwd()+'/'+filename)
print("Готово!")
my_file = open("PE.txt", "w")
my_file.write(ser_title)
my_file.write(ser_dat)
my_file.write(
	'\nАнонс: \n для ют. Православная энциклопедия ТВЦ \n для фб. #Православная_энциклопедия\n' + ser_anons + '\n')
my_file.write(ser_img[0] + '\n')
my_file.write(ser_vid[0])

my_file.close()
