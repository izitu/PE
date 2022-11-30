import os


f = open('OUTPUT\PE.txt', 'r')

# считываем все строки
lines = f.readlines()

# итерация по строкам
n = 0
for line in lines:
    n += 1
    if '***' in line:
        n = -2
    if n == 1:
        title = line.split('"')[1]
        print('title', title)
    if n == 2:
        date = line
        print('date', date)
    if n == 6:
        anons = line
        print('anons', anons)
    if n == 9:
        yt = line.split('/')[-1].split('\\')[0]
        print('yt', yt)
    # else:
    # print(n, line)


# закрываем файл
f.close