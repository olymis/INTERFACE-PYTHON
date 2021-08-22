from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('LightBlue')
layout = [
    [sg.Text('usuário'),sg.Input(key="Usuário")],
    [sg.Text('senha'),sg.Input(key='Senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')],

]

# janela

janela = sg.Window('Tela de login', layout)

# leitura de eventos

while True: 
    eventos, valores = janela.Read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'rafael' and valores ['Senha'] == '123456':
            print('SEJA BEM-VINDO')