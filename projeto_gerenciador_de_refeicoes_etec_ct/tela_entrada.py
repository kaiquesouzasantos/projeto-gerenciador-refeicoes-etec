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
senha_default = '123456789'

class TelaEntrada:
    def __init__(self):
        # janela --------------------------
        self.janela = Interface.func_retorna_janela(800, 400, 'Sistema de Controle')

        # variavel --------------------------
        self.ultima_atualizacao_data = str(Dados.func_carrega_dados(os.getcwd() + '/assets/dados/txt/ultima_atualizacao.txt'))

        # frame --------------------------
        self.frame = Interface.func_retorna_frame(self.janela, 800, 400)
        self.frame.pack(side = RIGHT)

        # componentes de frame --------------------------
        Interface.func_retorna_label(self.frame, 'ATUALIZAR INFORMACOES', 40, 150, 30)
        Interface.func_retorna_label(self.frame, 'A Ultima Atualizacao foi em ' + self.ultima_atualizacao_data, 10, 600, 370)

        self.senha = Interface.func_retorna_entrada(self.frame, 'Digite a Senha de Alteracao', 19, 600, 50, 100, 150)
        self.endereco = Interface.func_retorna_entrada(self.frame, 'Digite o Endereco Completo do Arquivo .txt', 19, 600, 50, 100,210)

        customtkinter.CTkButton(
            master=self.frame, text='Atualizar', width=600, fg_color='#00BF63',hover_color='#008243', text_color='#000', font=(fonte, 18),command=self.func_verifica_processo
        ).place(x=100, y=270)

        customtkinter.CTkButton(
            master=self.frame, text='<', fg_color='#FF3131', hover_color='#FF3131',width=40, height=40, font=(fonte, 15), command=self.func_retorna_inicio
        ).place(x=20, y=350)

    def func_verifica_processo(self):
        if(self.func_verifica_senha() != False):
            return
        
        threading.Thread(target = self.func_realiza_processo).start()

    def func_realiza_processo(self):
        if(proc_entrada_alunos(self.endereco.get())):
            Interface.func_retorna_label_colorida(self.frame, 'Nao Foi Possivel Encontrar o Arquivo', '#212121', 16, 100, 110)
            Interface.func_retorna_label_colorida(self.frame, 'A Base de Dados Foi Atualizada Com Sucesso', 'green', 16, 100, 110)

            self.janela.after(2000, self.rerun)
        else:
            Interface.func_retorna_label_colorida(self.frame, 'A Base de Dados Foi Atualizada Com Sucesso', '#212121', 16, 100, 110)
            Interface.func_retorna_label_colorida(self.frame, 'Nao Foi Possivel Encontrar o Arquivo', 'red', 16, 100, 110)

        self.senha.delete(0, END)
        self.endereco.delete(0, END)

    def func_verifica_senha(self):
        if(self.senha.get() != senha_default):
            Interface.func_retorna_label_colorida(self.frame, 'A Senha Informada Esta Incorreta', 'red', 16, 100, 110)
            return True
        else:
            Interface.func_retorna_label_colorida(self.frame, 'A Senha Informada Esta Incorreta', '#212121', 16, 100, 110)
            return False
        
    def rerun(self):
        self.janela.destroy()
        tela_entrada_rerun.rerun()
            
    def func_retorna_inicio(self):
        self.janela.destroy()
        tela_inicial.run()

# incializacao --------------------------

def run():
    TelaEntrada().janela.mainloop()