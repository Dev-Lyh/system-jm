import PySimpleGUI as sg


class Interface:
    def __init__(self):
        sg.theme('DarkBlue1')
        
        layout = [
            [sg.Radio('Modelo Antigo', 'Radio1', default=True, key='2007',font=('Calibri', 16), pad=(120,0)),
             sg.Radio('Modelo Atual', 'Radio1', key='2015',font=('Calibri', 16))],
            [sg.FileBrowse('Procurar arquivo', file_types=(("Arquivos PDF", '*.pdf')), size=(17,0),font=('Calibri', 14)), sg.Input(key='path',pad=(14,10),font=('Calibri', 14))],
            [sg.Text('Quantidade de páginas',font=('Calibri', 14),pad=(0,10)), sg.Input(key='pages',font=('Calibri', 14), size=(45,0),pad=(20,10))],
            [sg.Button('Concluir', expand_x=True, font=('Calibri', 14), pad=(0,20))]
        ]
        

        window = sg.Window(
            'Sistema de leitura de cartões ponto').layout(layout)

        self.button, self.values = window.Read()

    def Start(self):
        cp_one = self.values['2007']
        cp_two = self.values['2015']
        path = self.values['path']
        pages = self.values['pages']
        print(f'Model: {cp_one}-{cp_two}\r\nPath: {path}\r\nPages quantity: {pages}')


screen = Interface()
screen.Start()
