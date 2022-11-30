import os

pe_file = "PE0.txt"

# переделаем дату из файла 11 декабря 2021 в 06-12-2021 15:43:00
def modydate(ddd):
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                  'ноября', 'декабря']
    unzip_date = ddd.split(" ")
    # print(unzip_date)

    if unzip_date[2] in month_list:
        # print(month_list.index(unzip_date[2]) + 1)
        da_dat = f"{unzip_date[1]}-{month_list.index(unzip_date[2]) + 1}-{unzip_date[3][:-1]} 15:43:00"
        # print(da_dat)  # unzip_date[3][:-1] отрежем перевод строки
    else:
        print("нет такого месяца")
        exit(0)

    # print(month_list.index(unzip_date[1]))
    return da_dat

if os.path.exists(pe_file):
    print("Читаем файл")
    # получим объект файла
    file = open(pe_file, "r")

    # считываем все строки
    lines = file.readlines()

    # итерация по строкам
    for n, line in enumerate(lines):
        print(n, line)

    # закрываем файл
    file.close

    # 0 стр - название в кавычках -- выдернуть из кавычек
    # 1 стр - дата -- преобразовать в вид 06-12-2021 15:43:00
    # 5 стр - описание -- берем как есть
    # 6 стр - название картинки -- нужно выдернуть из урла

    tit = lines[0].split('"')[1]

    print(tit)

    print(modydate(lines[1]))

    print(lines[5][:-1])

    print(lines[6].split("/")[-1])

else:
    print("Файл не найден")

# print(lines[0])