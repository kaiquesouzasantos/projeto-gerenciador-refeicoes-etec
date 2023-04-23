from assets.modulo.tela import tela_erro, tela_inicial

try:
    tela_inicial.run()
except:
    tela_erro.run()