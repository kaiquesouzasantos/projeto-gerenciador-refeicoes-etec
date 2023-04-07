import os
import customtkinter
import threading
from tkinter import *

from assets.modulo.interface.Interface import Interface
from assets.modulo.funcionamento.Dados import Dados
from assets.proc_entrada import proc_entrada_alunos
import tela_inicial, tela_entrada_rerun

# config --------------------------
    
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# variaveis --------------------------

fonte = 'Roboto'

class TelaErro:
    def __init__(self):
        # janela --------------------------
        self.janela = Interface.func_retorna_janela(800, 400, 'Sistema de Controle')

        # frame --------------------------
        self.frame = Interface.func_retorna_frame(self.janela, 800, 400)
        self.frame.pack(side = RIGHT)

        # componentes de frame --------------------------
        Interface.func_retorna_label(self.frame, 'ERRO NA INICIALIZACAO', 40, 180, 30)
        Interface.func_retorna_label(self.frame, 'Nos desculpe, mas no momento de inicializacao do programa,', 18, 110, 120)
        Interface.func_retorna_label(self.frame, 'alguns componentes nao se comportaram como o esperado.', 18, 110, 147)
        Interface.func_retorna_label(self.frame, 'Tente realizar esses procedimentos:', 18, 110, 174)
        Interface.func_retorna_label(self.frame, '      - Verifique se outro programa esta utilizando a camera.', 18, 110, 201)
        Interface.func_retorna_label(self.frame, '      - Reinicie o programa/computador.', 18, 110, 228)
        Interface.func_retorna_label(self.frame, '      - Se o problema persistir, contate o responsavel pela aplicacao.', 18, 110, 255)

        customtkinter.CTkButton(
            master=self.frame, text='Fechar Programa', width=600, fg_color='#FF3131',hover_color='#FF3131', text_color='#000', font=(fonte, 18),command=self.func_fecha_aplicacao
        ).place(x=100, y=330)

    def func_fecha_aplicacao(self):
        self.janela.destroy()

# incializacao --------------------------

def run():
    TelaErro().janela.mainloop()