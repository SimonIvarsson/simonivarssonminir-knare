import PySimpleGUI as sg 
import webbrowser

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font= 'Impact 14', button_element_size = (6,3))
    button_size = (12,3)
    layout = [
        [sg.Text(
            '',
            font = 'Impact 26', 
            justification = 'right', 
            expand_x = True, 
            pad = (10,20),
            right_click_menu = theme_menu,
            key = '-TEXT-')
        ],
        [sg.Button('Rensa', expand_x = True, button_color = None), sg.Button('Enter', expand_x = True)],
        [sg.Button(5, size = button_size), sg.Button(8, size = (3,4)), sg.Button(9, size = button_size), sg.Button('*', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(7, size = button_size), sg.Button(1, size = (2,7)), sg.Button('/', size = button_size)],
        [sg.Button(6, size = (5,6)), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button('.', size = (7,4)), sg.Button('+', size = button_size)],
        [sg.Button('Hjälp', key = '-LINK-',expand_x = True), sg.Button('Städa', expand_x = True)]

    ]

    return sg.Window('Miniräknare', layout, 'Button Color')

theme_menu = ['menu', ['BrownBlue', 'dark', 'Darkgray8', 'random']]
window = create_window('Purple')

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8',  '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)

    if event in ['+', '-', '/', '*']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-TEXT-'].update('')

    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result = eval(''.join(full_operation))
        window['-TEXT-'].update(result)
        full_operation = []

    if event == 'Rensa':
        current_num = []
        full_operation = []
        window['-TEXT-'].update('')
    
    if event == '-LINK-':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
    if event == 'Städa':
        window.close()
        def create_window(theme):
            sg.theme(theme)
            sg.set_options(font= 'Impact 14', button_element_size = (6,3))
            button_size = (12,3)
            layout = [
            [sg.Text(
                '',
                font = 'Impact 26', 
                justification = 'right', 
                expand_x = True, 
                pad = (10,20),
                right_click_menu = theme_menu,
                key = '-TEXT-')
            ],
            [sg.Button('Rensa', expand_x = True, button_color = None), sg.Button('Enter', expand_x = True)],
            [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', size = button_size)],
            [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('/', size = button_size)],
            [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
            [sg.Button(0, expand_x = True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)],
            [sg.Button('Hjälp', key = '-LINK-',expand_x = True)]

        ]   

            return sg.Window('Miniräknare', layout, 'Button Color')

        theme_menu = ['menu', ['BrownBlue', 'dark', 'Darkgray8', 'random']]
        window = create_window('BrownBlue')

        current_num = []
        full_operation = []

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event in theme_menu[1]:
                window.close()
                window = create_window(event)

            if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8',  '9', '.']:
                current_num.append(event)
                num_string = ''.join(current_num)
                window['-TEXT-'].update(num_string)

            if event in ['+', '-', '/', '*']:
                full_operation.append(''.join(current_num))
                current_num = []
                full_operation.append(event)
                window['-TEXT-'].update('')

            if event == 'Enter':
                full_operation.append(''.join(current_num))
                result = eval(''.join(full_operation))
                window['-TEXT-'].update(result)
                full_operation = []

            if event == 'Rensa':
                current_num = []
                full_operation = []
                window['-TEXT-'].update('')
    
            if event == '-LINK-':
                webbrowser.open('https://www.youtube.com/jonasvikstrom')            

    
window.close()