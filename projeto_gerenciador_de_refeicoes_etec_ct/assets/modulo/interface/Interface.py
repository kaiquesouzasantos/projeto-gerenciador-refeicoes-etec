import customtkinter
from tkinter import *

class Interface:
    def func_centraliza_tela(largura, altura):
        root = Tk()
        monitor_altura, monitor_largura = root.winfo_screenheight(), root.winfo_screenwidth()
        root.destroy()

        posicao_x = monitor_largura/2 - largura/2
        posicao_y = monitor_altura/2 - altura/2

        return '%dx%d+%d+%d' % (largura, altura, posicao_x, posicao_y-50)


    def func_retorna_janela(largura, altura, titulo):
        janela = customtkinter.CTk()
        #janela.geometry(f'{largura}x{altura}')
        janela.geometry(Interface.func_centraliza_tela(largura, altura))
        janela.title(titulo)
        # janela.iconitmap('<icone>')
        janela.resizable(False, False) # ajuste de tamanho

        return janela
    
    def func_retorna_frame(janela, largura, altura):
        return customtkinter.CTkFrame(master = janela, width = largura, height = altura)

    def func_retorna_imagem(janela, endereco_imagem, x_, y_):
        imagem = customtkinter.CTkLabel(master = janela, image = PhotoImage(file = endereco_imagem), text = '')
        imagem.place(x = x_, y = y_)

        return imagem
    
    def func_retorna_imagem_pr(janela, endereco_imagem):
        imagem = customtkinter.CTkLabel(master = janela, image = PhotoImage(file = endereco_imagem), text = '')

        return imagem

    def func_retorna_label(frame, texto, tamanho_fonte, x_, y_):
        label = customtkinter.CTkLabel(master = frame, text = texto, font=('Roboto', tamanho_fonte))
        label.place(x = x_, y = y_)

        return label
    
    def func_retorna_label_colorida(frame, texto, cor, tamanho_fonte, x_, y_):
        label = customtkinter.CTkLabel(master = frame, text = texto, font=('Roboto', tamanho_fonte), text_color = cor)
        label.place(x = x_, y = y_)

        return label

    def func_retorna_entrada(frame, placeholder, tamanho_fonte, largura, altura, x_, y_):
        entrada = customtkinter.CTkEntry(master = frame, placeholder_text = placeholder, width = largura, height = altura, font=('Roboto', tamanho_fonte))
        entrada.place(x = x_, y = y_)

        return entrada