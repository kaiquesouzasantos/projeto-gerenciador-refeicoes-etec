class Dados:
    def func_carrega_dados(endereco):
        arquivo = open(endereco, "r")
        linhas = [linha.rstrip() for linha in arquivo.readlines()]
        arquivo.close()

        return linhas
