import os
import customtkinter
from tkinter import *

from assets.modulo.interface.Interface import Interface
from assets.modulo.tela import tela_inicial
from assets.modulo.procedimento import encerra_processo

# config --------------------------

customtkinter.set_appearance_mode('light') # System
customtkinter.set_default_color_theme('dark-blue')

# variavel --------------------------

fonte = 'Roboto'

class TelaDesenvolvedor:
    def __init__(self):
        # janela --------------------------
        self.janela = Interface.func_retorna_janela(800, 400, 'Sistema de Controle | Desenvolvedor')
        self.janela.protocol("WM_DELETE_WINDOW", encerra_processo.encerra)

        # img default --------------------------
        Interface.func_retorna_imagem(self.janela, os.getcwd() + '/assets/dados/desenvolvedor.png', 0, 0)

        # frame --------------------------
        self.frame = Interface.func_retorna_frame(self.janela, 450, 400)
        self.frame.pack(side = RIGHT)

        # componentes de frame --------------------------
        Interface.func_retorna_label(self.frame, 'Kaique Souza Santos', 40, 20, 80)
        Interface.func_retorna_label(self.frame, 'MTEC - Desenvolvimento de Sistemas (2021 - 2023)', 15, 20, 130)
        Interface.func_retorna_label(self.frame, 'Linkedin: linkedin.com/in/kaique-souza-santos/', 15, 20, 150)
        Interface.func_retorna_label(self.frame, 'Github: github.com/kaiquesouzasantos', 15, 20, 170)

        Interface.func_retorna_label(self.frame, 'Professores Orientadores: ', 15, 18, 220)
        Interface.func_retorna_label(self.frame, '-   Danadoni Lima dos Santos', 15, 18, 240)
        Interface.func_retorna_label(self.frame, '-   Everson Willian Pereira Bacelli', 15, 18, 260)
        Interface.func_retorna_label(self.frame, '-   Thayani da Silva Pereira', 15, 18, 280)

        customtkinter.CTkButton(master=self.frame, text='<', fg_color='#FF3131', hover_color='#FF3131',width=40, height=40, font=(fonte, 15), command=self.func_retorna_inicio).place(x=20, y=350)

    def func_retorna_inicio(self):
        self.janela.destroy()
        tela_inicial.run()

# inicializacao --------------------------
def run():
    TelaDesenvolvedor().janela.mainloop()