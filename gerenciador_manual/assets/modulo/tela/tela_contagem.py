import os
import customtkinter
from tkinter import *
import threading

from assets.modulo.interface.Interface import Interface
from assets.modulo.funcionamento.Data import Data
from assets.modulo.funcionamento.Dados import Dados
from assets.proc_contagem import *
from assets.modulo.reinicializacao import tela_contagem_rerun
from assets.modulo.tela import tela_inicial

# config --------------------------

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')

# variavel --------------------------

fonte = 'Roboto'

class TelaContagem:
    def __init__(self):
        # janela --------------------------
        self.janela = Interface.func_retorna_janela(800, 400, 'Sistema de Controle | Contagem de Refeicoes')

        # img default --------------------------
        Interface.func_retorna_imagem(self.janela, os.getcwd() + '/assets/dados/img_processo/proc_aguardando.png', 0, 0)

        # variaveis --------------------------
        self.data_atual = Data.func_retorna_data()
        self.periodo_atual = Data.func_retorna_periodo_str()
        self.ultima_leitura_tempo = Data.func_retorna_periodo_segundo()
        self.refeicoes_servidas = str(
            int(
                len(Dados.func_carrega_dados(os.getcwd() + '/assets/dados/restauracao/arquivo_restauracao.txt')) +
                len(Dados.func_carrega_dados(os.getcwd() + '/assets/dados/restauracao/arquivo_repeticao_restauracao.txt'))
            )
        )

        # frame --------------------------=
        self.frame_1 = Interface.func_retorna_frame(self.janela, 800, 250)
        self.frame_1.place(x=0, y=150)

        # componentes de frame --------------------------

        # LINHA 1
        customtkinter.CTkButton(
            master=self.frame_1, text='Ultima Execucao',width=200, font=(fonte, 18), fg_color='#424040', hover_color='#424040'
        ).place(x=50, y=20)

        customtkinter.CTkButton(
            master=self.frame_1, text=self.ultima_leitura_tempo,width=135, font=(fonte, 18), fg_color='#BAB3B3', hover_color='#BAB3B3', text_color='#424040'
        ).place(x=245, y=20)

        # LINHA 2
        customtkinter.CTkButton(
            master=self.frame_1, text='Refeicoes Servidas', width=200,font=(fonte, 18), fg_color='#424040', hover_color='#424040'
        ).place(x=50, y=60)

        customtkinter.CTkButton(
            master=self.frame_1, text=self.refeicoes_servidas,width=135, font=(fonte, 18), fg_color='#BAB3B3', hover_color='#BAB3B3', text_color='#424040'
        ).place(x=245, y=60)

        # LINHA 3
        customtkinter.CTkButton(
            master=self.frame_1, text='Data', width=200, font=(fonte, 18),fg_color='#424040', hover_color='#424040'
        ).place(x=50, y=100)

        customtkinter.CTkButton(
            master=self.frame_1, text=self.data_atual,width=135, font=(fonte, 18), fg_color='#BAB3B3', hover_color='#BAB3B3', text_color='#424040'
        ).place(x=245, y=100)

        # LINHA 4
        customtkinter.CTkButton(
            master=self.frame_1, text='Periodo', width=200, font=(fonte, 18),fg_color='#424040', hover_color='#424040'
        ).place(x=50, y=140)

        customtkinter.CTkButton(
            master=self.frame_1, text=self.periodo_atual,width=135, font=(fonte, 18), fg_color='#BAB3B3', hover_color='#BAB3B3', text_color='#424040'
        ).place(x=245, y=140)

        # COLUNA 2
        customtkinter.CTkButton(
            master=self.frame_1, text='Ler QR CODE', width=335, height=150,font=(fonte, 20), fg_color='#FF3131', hover_color='#D82121',text_color='#000', command=self.func_contagem
        ).place(x=415, y=20)

        # LINHA 5
        customtkinter.CTkButton(
            master=self.frame_1, text='Finalizar Contagem', width=700, font=(fonte, 20),fg_color='#00BF63', hover_color='#008243', text_color='#000',command=self.func_finaliza_processo
        ).place(x=50, y=200)

    def rerun(self):
        self.janela.destroy()
        tela_contagem_rerun.rerun()

    def func_contagem(self):
        Interface.func_retorna_imagem(self.janela, os.getcwd() + '/assets/dados/img_processo/proc_lendo.png', 0, 0)
        threading.Thread(target = self.func_atualiza_processo).start()

    def func_atualiza_processo(self):
        if (proc_contagem()):
            Interface.func_retorna_imagem(self.janela, os.getcwd() + '/assets/dados/img_processo/proc_aprovado.png', 0, 0)
            self.janela.after(2000, self.rerun)
        else:
            Interface.func_retorna_imagem(self.janela, os.getcwd() + '/assets/dados/img_processo/proc_negado.png', 0, 0)
            self.janela.after(2000, self.rerun)


    def func_verifica_funcionamento(self):
        if (Data.func_retorna_periodo_str() == 'Fora de Servico' and self.refeicoes_servidas == 0):
            self.janela.destroy()
            os.system('python ' + os.getcwd() + '/tela_inicial.py')

    def func_finaliza_processo(self):
        proc_finaliza_contagem()
        self.janela.destroy()
        tela_inicial.run()

# incializacao --------------------------
def run():
    #TelaContagem().func_verifica_funcionamento()
    TelaContagem().janela.mainloop()