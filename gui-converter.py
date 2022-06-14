import PySimpleGUI as sg
# 1km = 0.6214 / 1kg = 2.20462
layout = [
    [
        sg.Text('Выберете единицу измерения', enable_events = True, key = '-TEXT-'), 
        sg.Spin(['km', 'mil', 'kg', 'pou'], key = '-ED-')
    ],
    [sg.Input(key = '-INPUT-')],
    [
        sg.Button('Конвертировать', key = '-BUTTON-'), 
        sg.Text('Здесь будет результат', key = '-REZULT-', visible = False)
    ],
]

window = sg.Window('Конвертер', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-TEXT-':
        print(values)
        print(values['-ED-'])

    if event == '-BUTTON-' and values['-INPUT-'] != '':
        window['-REZULT-'].update(visible = True)
