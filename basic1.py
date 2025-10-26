import FreeSimpleGUI as sg

# filename = sg.popup_get_file('Enter the file you wish to process')
# sg.popup('You entered', filename)
           

menu_def = [['File', ['Embeded', 'Ekstraksi',]],
            ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
            ['About',[]]]

tombolMenu = [
    [sg.B('Embebded'),sg.B('Ekstraksi')]
]

layout = [tombolMenu]

window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying FreeSimpleGUI")

# Finish up by removing from the screen
window.close()