import bs4
import os
import requests
import wget

SER_NUM = 1
DIR = 'OUTPUT'
URL = 'http://www.tvc.ru/channel/brand/id/14'
os.chdir(DIR)
print(os.getcwd())

page_html = requests.get(URL)
page_soup = bs4.BeautifulSoup(page_html.text, "html.parser")
# получаем адрес серии
p_block = page_soup.find_all('a', {'class': 'series__link-block'})
print(SER_NUM)
# print(p_block)
# print(len(p_block))
print('*' * 20)
my_file = open("PE.txt", "w")
for item in p_block[:SER_NUM]:
    url_ser = 'http://www.tvc.ru' + item.get('href')
    print(url_ser)
    ser_html = requests.get(url_ser)
    ser_soup = bs4.BeautifulSoup(ser_html.text, "html.parser")

    ser_title = ser_soup.find('meta', property='og:title').get('content')
    print(ser_title)

    ser_anons = ser_soup.find('meta', property='og:description').get('content')
    print(ser_anons)

    img_url = ser_soup.find('meta', property='og:image').get('content')
    print(img_url)

    video_url_raw = (
        ser_soup.find('meta', property='og:video')
        .get('content').replace('iframe', 'json'))
    print(video_url_raw)

    dat_raw = ser_soup.select('.article__day')
    # первый элемент - день недели - берем только текст и удаляем
    # справа все не нужное (перевод стороки)
    # плюс пробел
    # второй элемент - удаляем повторяющиеся пробелы из текста
    ser_dat = (
        dat_raw[0].getText().rstrip() + ' ' + " "
        .join(dat_raw[1].getText().split()))
    print(ser_dat)
    wget.download(img_url)

    # Переходим на json ссылку и вынимаем прямой урл
    soup = requests.get(video_url_raw).json()
    video_url = soup['path']['quality'][0]['url']
    wget.download(video_url)

    my_file.write(ser_title)
    my_file.write(ser_dat)
    my_file.write('\nАнонс: \nПравославная энциклопедия ТВЦ \n'
                  + ser_anons+'\n')
    my_file.write(img_url + '\n')
    my_file.write(video_url + '\n')
    my_file.write('*' * 50 + '\n\n\n')

my_file.close()
