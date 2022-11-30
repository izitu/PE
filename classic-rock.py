# https://www.loudersound.com/classic-rock/news
import requests
import bs4
import os
import wget
import sqlite3
from sqlite3 import Error
import string

def sql_connection():
    try:
        con = sqlite3.connect('db.sqlite3')
        return con
    except Error:
        print(Error)

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO posts_post(text, author_id, group_id, image, pub_date) VALUES(?, ?, ?, ?, ?)', entities)
    con.commit()

def izin(full_name):
    if os.path.exists(f"OUTPUT/{full_name}"):
        print(f"OUTPUT/{full_name} есть!")
        return True
    else:
        return False

auth = {
    'Fraser Lewry': 10,
    'Liz Scarlett': 11,
    'Scott Munro': 12,
    'Natasha Scharf': 13,
    'Merlin Alderslade': 14,
    'Paul Brannigan': 15,
    'Metal Hammer': 16,
    'Classic Rock Magazine': 17,
    'Louder': 18,
    'Simon Young': 19,
    'Rich Hobson': 20,
    'Classic Rock': 21,
}

cat = {
    'Prog': 10,
    'Classic Rock': 11,
    'Metal Hammer': 12,
    'Louder': 13,
}

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)


con = sql_connection()


# exit(0)

urls = {'https://www.loudersound.com/classic-rock/news': 'i1.html',
        'https://www.loudersound.com/classic-rock/news/page/2': 'i2.html',}
for url in urls:
    print(url, urls[url])

    if not izin(urls[url]):
        req = requests.get(url)
        req.encoding = 'utf-8'
        src = req.text
        print(f'Скачиваем {url} сюда -> OUTPUT/{urls[url]}')
        with open(f'OUTPUT/{urls[url]}', 'w', encoding='utf-8') as file:
            file.write(src)

    with open(f'OUTPUT/{urls[url]}', encoding='utf-8') as file:
                src = file.read()

    soup = bs4.BeautifulSoup(src, "html.parser")
    marks = soup.find_all("div", class_="listingResult")#.find_all('a')
    for mark in marks:
        # # print('-'*10)
        title = mark.find("h3", class_="article-name")
        if title:
            # print('title: ', title.text)
            all_txt = title.text
        sinopsis = mark.find("p", class_="synopsis")
        if sinopsis:
            # print('sinopsis: ', sinopsis.text)
            all_txt += sinopsis.text
        print('title:', all_txt)
        if mark.find("p", class_="byline"):
            name = mark.find("p", class_="byline").find_all("span")[1].text
            name = ''.join(c for c in name if c in valid_chars).strip()
            print(name, auth[name])
        # #     # print(mark.find("p", class_="byline").text)
            pub_date = mark.find("p", class_="byline").find("time").get("datetime").replace('T', ' ').replace('Z', '')
            print(pub_date)
        if mark.find("a", class_="category-link"):
            category_name = mark.find("a", class_="category-link").text
            category_id = cat[category_name]
            print(category_id, category_name)
        img = mark.find("figure", class_="article-lead-image-wrap")
        if img:
            # print(mark.find("figure", class_="article-lead-image-wrap").get("data-original"))
            # wget.download(str(mark.find("figure", class_="article-lead-image-wrap").get("data-original")))
            img_path = f'posts/{img.get("data-original").split("/")[-1]}'
            print(img_path)
        # text = 'lorem'
        # pub_date = '2022-09-21 10:00:00'
        # image = 'posts/coF3c4WDjiQgvP5n2WD4uc.jpg'
        sql_insert(con, [all_txt, auth[name], category_id, img_path, pub_date])
con.close()