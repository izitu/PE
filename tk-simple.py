import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True, key = '-TEXT-'), sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Обновить текст', key = '-BUTTON1-')],
    [sg.Input(key = '-INPUT-')],
    [sg.Text('тест'), sg.Button('Кнопка', key = '-BUTTON2-')]
]
window = sg.Window('Православная энциклопедия', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-TEXT-'].update(values['-INPUT-'])

    if event == '-BUTTON2-':
        print('Бууууу!')    

    if event == '-TEXT-':
        print(values)            

window.close()