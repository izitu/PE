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

exit(0)
for datt in dat_raw:
    # и удаляем пробелы
    dat = dat + " ".join(datt.getText().split())
    print(dat)
print(dat_raw)
print(dat)
exit(0)
p_tit=b.select('.series__item .series__item-title')
ser_title=p_tit[0].getText()
p_dat=b.select('.series__month-day .series__item-month')
ser_dat=p_dat[0].getText()
print('Последняя серия :' + ser_title + '  дата:'+ser_dat)
print("--------")
exit(0)
# получаем адрес серии
p_block=b.select('.series__link-block')

string=p_block[0]
result=re.findall(fnd_href,str(string))
print(result[0])

# скачиваем
s1=requests.get('http://www.tvc.ru'+result[0])
p=bs4.BeautifulSoup(s1.text, "html.parser")

# получаем анонс
p_anons=p.select('.brand__anons-text')
ser_anons=p_anons[0].getText()
print('Анонс: \n для ют. Православная энциклопедия ТВЦ \n для фб. #Православная_энциклопедия\n' + ser_anons)
p_player=p.select('.brand__player-inner')


result=re.findall(fnd_src,str(p_player))
print(result[0])
print('http://www.tvc.ru'+result[0])

driver = webdriver.Firefox()
driver.get('http://www.tvc.ru'+result[0])
time.sleep(5)
htmlSource = driver.page_source
#print(htmlSource)
driver.close()

ser_vid=re.findall(fnd_sosrc,str(htmlSource))
print(ser_vid[0])
print('Скачиваем!!!!')
filename = wget.download(ser_vid[0])
os.rename(filename, u''+os.getcwd()+'/'+filename)
print("Готово!")
my_file = open("PE.txt", "w")
my_file.write(ser_title)
my_file.write(ser_dat)
my_file.write('\nАнонс: \n для ют. Православная энциклопедия ТВЦ \n для фб. #Православная_энциклопедия\n' + ser_anons+'\n')
my_file.write(ser_img[0]+'\n')
my_file.write(ser_vid[0])

my_file.close()
