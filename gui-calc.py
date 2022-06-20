import PySimpleGUI as sg

sg.theme('DarkBlue1')
sg.set_options(font = 'Franklin 14', button_element_size= (6, 1))
layout = [
    [sg.Text('output')],
    [sg.Button('Clear'), sg.Button('Enter')],
    [sg.Button(7), sg.Button(8), sg.Button(9), sg.Button('*')],
    [sg.Button(4), sg.Button(5), sg.Button(6), sg.Button('/')],
    [sg.Button(1), sg.Button(2), sg.Button(3), sg.Button('-')],
    [sg.Button(0), sg.Button('.'), sg.Button('+')],
]


window = sg.Window('Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()