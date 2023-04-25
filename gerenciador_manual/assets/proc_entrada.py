import os
from assets.modulo.funcionamento.Arquivo import Arquivo as arquivo
from assets.modulo.funcionamento.QRCode import QRCode as qrCode
from assets.modulo.funcionamento.Dados import Dados as dados
from assets.modulo.funcionamento.Email import Email as smtp
from assets.modulo.funcionamento.Criptografia import Criptografia as cripto

def proc_entrada_alunos(endereco_recebido):
    endereco = proc_troca_barras_endereco(endereco_recebido)
    
    if(len(endereco) == 0):
        return False

    try:
        entrada = list(set(dados.func_carrega_dados(endereco)))
        arquivo.func_escreve_dados(entrada)
        arquivo.func_escreve_dados_criptografados(entrada)
        arquivo.func_exclui_qrcodes()
        qrCode.func_gera_qrcodes(dados.func_carrega_dados(os.getcwd() + '/assets/dados/txt/alunos_cripto.txt'))
        proc_envia_qrcode_email(dados.func_carrega_dados(os.getcwd() + '/assets/dados/txt/alunos_email.txt'))
        arquivo.func_ultima_atualizacao_alunos()
        arquivo.func_escreve_titulo_relatorio()

        return True
    except:
        return False

def proc_troca_barras_endereco(endereco):
    saida = ''

    for caracter in endereco:
        if(caracter == '\\'):
            saida += '/'
        else:
            saida += caracter

    return fr'{saida}'

def proc_envia_qrcode_email(emails):
    for email in emails:
        smtp.envia_email(email, cripto.func_criptografa(email))