import os

from assets.modulo.funcionamento.Dados import Dados as dados
from assets.modulo.funcionamento.Compara import Compara as compara
from assets.modulo.funcionamento.Criptografia import Criptografia as cripto

def proc_busca_por_email(email):
    entrada_cripto = cripto.func_criptografa(email)
    alunos_dados = dados.func_carrega_dados(os.getcwd() + '/assets/dados/txt/alunos_cripto.txt')

    if(compara.func_retorna_existencia_cadastro(entrada_cripto, alunos_dados)):
        return  os.getcwd() + '/assets/dados/qr_code/' + entrada_cripto + '.png'
    else:
        return False