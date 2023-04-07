import os

from assets.modulo.funcionamento.Arquivo import Arquivo as arquivo
from assets.modulo.funcionamento.QRCode import QRCode as qrCode
from assets.modulo.funcionamento.Dados import Dados as dados

def proc_entrada_alunos(endereco_recebido):
    endereco = proc_troca_barras_endereco(endereco_recebido)

    try:
        entrada = dados.func_carrega_dados(endereco)
        arquivo.func_escreve_dados(entrada)
        arquivo.func_escreve_dados_criptografados(entrada)
        arquivo.func_ultima_atualizacao_alunos()
        arquivo.func_exclui_qrcodes()
        qrCode.func_gera_qrcodes(dados.func_carrega_dados(os.getcwd() + '/assets/dados/txt/alunos_cripto.txt'))
        arquivo.func_escreve_titulo_relatorio()

        return True
    except Exception as e:
        return False

def proc_troca_barras_endereco(endereco):
    saida = ''

    for caracter in endereco:
        if(caracter == '\\'):
            saida += '/'
        else:
            saida += caracter

    return fr'{saida}'

