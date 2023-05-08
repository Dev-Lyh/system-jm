import PySimpleGUI as sg

def open(index, all_pages):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text(f'{index}', key='ind')],
                [sg.Text(f'{all_pages}', key='all')]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=2)
        window['ind'].update(index)
        window['all'].update(all_pages)
        