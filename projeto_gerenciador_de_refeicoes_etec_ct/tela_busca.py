import os
import customtkinter
from tkinter import *

from assets.modulo.interface.Interface import Interface
from assets.proc_busca import proc_busca_por_email
import tela_inicial, tela_busca_rerun

# config --------------------------

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# variavel --------------------------

fonte = 'Roboto'

class TelaBusca:
    def __init__(self):
        # janela --------------------------
        self.janela = Interface.func_retorna_janela(800, 400, 'Sistema de Controle')

        # img default ------------------------
        Interface.func_retorna_imagem(self.janela, os.getcwd() + '/assets/dados/qr_code_default/qrcode_default.png', 42.5, 65)

        # frame --------------------------
        self.frame = Interface.func_retorna_frame(self.janela, 450, 400)
        self.frame.pack(side=RIGHT)

        # componentes de frame --------------------------
        Interface.func_retorna_label(self.frame, 'BUSCA POR EMAIL', 40, 60, 30)

        self.email = Interface.func_retorna_entrada(self.frame, 'Digite o Email Institucional', 19, 390, 50, 30, 170)

        customtkinter.CTkButton(master=self.frame, text='Buscar', fg_color='#00BF63', hover_color='#008243',text_color='#000', width=390, font=(fonte, 18), command=self.func_verificar).place(x=30, y=230)
        customtkinter.CTkButton(master=self.frame, text='<', fg_color='#FF3131', hover_color='#FF3131',width=40, height=40, font=(fonte, 15), command=self.func_retorna_inicio).place(x=20, y=350)

    def retorna_janela(self):
        return self.janela

    def rerun(self):
        self.janela.destroy()
        tela_busca_rerun.rerun()

    def func_verificar(self):
        imagem = proc_busca_por_email(self.email.get())

        if (imagem):
            Interface.func_retorna_imagem(self.janela, imagem, 42.5, 65)
            Interface.func_retorna_label_colorida(self.frame, 'O Email nao foi encontrado', '#212121', 16, 30, 140)
            Interface.func_retorna_label_colorida(self.frame, self.email.get() + ' encontrado com sucesso', '#00BF63', 16, 30,140)
            self.email.delete(0, END)
        else:
            self.janela.after(1, self.rerun)

    def func_retorna_inicio(self):
        self.janela.destroy()
        tela_inicial.run()

# incializacao --------------------------
def run():
    TelaBusca().janela.mainloop()