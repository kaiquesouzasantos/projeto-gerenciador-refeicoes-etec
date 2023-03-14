import cv2
import os
from pyzbar.pyzbar import decode

from assets.modulo.funcionamento.Compara import Compara as compara
from assets.modulo.funcionamento.Dados import Dados as dados
from assets.modulo.funcionamento.Arquivo import Arquivo as relatorio
from assets.modulo.funcionamento.Data import Data as data

alunos_dados = dados.func_carrega_dados(os.getcwd() + '/assets/dados/txt/alunos_cripto.txt')
alunos_contabilizados = dados.func_carrega_dados(os.getcwd() + '/assets/dados/restauracao/arquivo_restauracao.txt')

if len(alunos_contabilizados) == 0:
    alunos_contabilizados = list()

periodo_inicio = data.func_retorna_periodo()
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def proc_contagem():
    validade = None

    while(validade == None):
        sucess, img = captura.read()

        for barcode in decode(img):
            codigo = barcode.data.decode('utf-8')
            validade = compara.func_compara(codigo, alunos_dados, alunos_contabilizados)

            if(validade):
                alunos_contabilizados.append(codigo)
                relatorio.func_ponto_restauracao_consumo(alunos_contabilizados)

    return validade

def proc_finaliza_contagem():
    relatorio.func_escreve_relatorio(periodo_inicio, len(alunos_contabilizados))
            
