import os
import customtkinter
from tkinter import *

from assets.modulo.interface.Interface import Interface
from assets.modulo.tela import tela_desenvolvedor, tela_busca, tela_entrada, tela_contagem

# config --------------------------

customtkinter.set_appearance_mode('light') # System
customtkinter.set_default_color_theme('dark-blue')

# variavel --------------------------

fonte = 'Roboto'

class TelaInicial:
    def __init__(self):
        # janela --------------------------
        self.janela = Interface.func_retorna_janela(800, 400, 'Sistema de Controle')

        # img default --------------------------
        Interface.func_retorna_imagem(self.janela, os.getcwd() + '/assets/dados/logo.png', 0, 0)

        # frame --------------------------
        self.frame = Interface.func_retorna_frame(self.janela, 450, 400)
        self.frame.pack(side = RIGHT)

        # componentes de frame --------------------------
        Interface.func_retorna_label(self.frame, 'PAGINA INICIAL', 40, 80, 40)

        customtkinter.CTkButton(
            master=self.frame, text='Iniciar Contagem', width=390, height=50,fg_color='#BAB3B3', hover_color='#424040', text_color='#000',font=(fonte, 20), command=self.func_abre_contagem
        ).place(x=30, y=130)

        customtkinter.CTkButton(
            master=self.frame, text='Buscar QR Code Por Email', width=390, height=50,fg_color='#BAB3B3', hover_color='#424040', text_color='#000',font=(fonte, 20), command=self.func_abre_busca
        ).place(x=30, y=200)

        customtkinter.CTkButton(
            master=self.frame, text='Atualizar Alunos', width=390, height=50,fg_color='#BAB3B3', hover_color='#424040', text_color='#000',font=(fonte, 20), command=self.func_abre_atualizacao
        ).place(x=30, y=270)

        customtkinter.CTkButton(
            master=self.frame, text='Desenvolvedor', width=390, height=20,fg_color='#e5e5e5', hover_color='#e5e5e5', text_color='#000',font=(fonte, 15), command=self.func_abre_desenvolvedor
        ).place(x=30, y=350)

    def func_abre_contagem(self):
        self.janela.destroy()
        tela_contagem.run()

    def func_abre_busca(self):
        self.janela.destroy()
        tela_busca.run()

    def func_abre_atualizacao(self):
        self.janela.destroy()
        tela_entrada.run()

    def func_abre_desenvolvedor(self):
        self.janela.destroy()
        tela_desenvolvedor.run()

# inicializacao --------------------------
def run():
    TelaInicial().janela.mainloop()