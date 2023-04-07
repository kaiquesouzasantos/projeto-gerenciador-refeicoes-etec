import csv
from os import path
import os

from assets.modulo.funcionamento.Data import Data 
from assets.modulo.funcionamento.Criptografia import Criptografia 

class Arquivo:
    def func_escreve_relatorio(periodo_incio, contagem, repeticao):
        arquivo = open(path.join(path.expanduser("~"), "Documents/contagem.csv"), 'a')
        escreve = csv.writer(arquivo)

        escreve.writerow([f'{Data.func_retorna_data()}; {periodo_incio}; {Data.func_retorna_periodo()}; {contagem}; {repeticao}'])
        Arquivo.func_limpa_restauracao()
        Arquivo.func_limpa_repeticao_restauracao()

    def func_escreve_titulo_relatorio():
        arquivo = open(path.join(path.expanduser("~"), "Documents/contagem.csv"), 'w')
        escreve = csv.writer(arquivo)

        escreve.writerow(['DATA; HORARIO DE INICIO; HORARIO DE FINALIZACAO; REFEICOES; REPETICOES;'])

    def func_escreve_dados(alunos):
        arquivo = open(os.getcwd() + '/assets/dados/txt/alunos_email.txt', 'w')
        
        for aluno in alunos:
            arquivo.write(f'{aluno}\n')

    def func_escreve_dados_criptografados(alunos):
        arquivo = open(os.getcwd() + '/assets/dados/txt/alunos_cripto.txt', 'w')
        
        for aluno in alunos:
            aluno_criptografado = Criptografia.func_criptografa(aluno)
            arquivo.write(f'{aluno_criptografado}\n')

    def func_ponto_restauracao_consumo(alunos):
        arquivo = open(os.getcwd() + '/assets/dados/restauracao/arquivo_restauracao.txt', 'w')
        
        for aluno in alunos:
            arquivo.write(f'{aluno}\n')

    def func_ponto_restauracao_repeticao_consumo(alunos):
        arquivo = open(os.getcwd() + '/assets/dados/restauracao/arquivo_repeticao_restauracao.txt', 'w')
        
        for aluno in alunos:
            arquivo.write(f'{aluno}\n')

    def func_limpa_restauracao():
        Arquivo.func_escreve_linha_unica(os.getcwd() + '/assets/dados/restauracao/arquivo_restauracao.txt', '')

    def func_limpa_repeticao_restauracao():
        Arquivo.func_escreve_linha_unica(os.getcwd() + '/assets/dados/restauracao/arquivo_repeticao_restauracao.txt', '')

    def func_ultima_atualizacao_alunos():
        Arquivo.func_escreve_linha_unica(os.getcwd() + '/assets/dados/txt/ultima_atualizacao.txt', Data.func_retorna_data())

    def func_exclui_qrcodes():
        local = os.getcwd() + '/assets/dados/qr_code/'

        for arquivo in os.listdir(local):
            os.remove(os.path.join(local, arquivo))

    def func_escreve_linha_unica(endereco, conteudo):
        arquivo = open(endereco, 'w')
        arquivo.write(conteudo)