import PySimpleGUI as sg
# 1km = 0.6214 / 1kg = 2.20462
layout = [
    [sg.Text('Выберете единицу измерения', enable_events = True, key = '-TEXT-'), sg.Spin(['km', 'mil', 'kg', 'pou'])],
    [sg.Button('Обновить текст', key = '-BUTTON1-')],
    [sg.Input(key = '-INPUT-')],
    [sg.Text('тест'), sg.Button('Кнопка', key = '-BUTTON2-')]
]

window = sg.Window('Конвертер', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break