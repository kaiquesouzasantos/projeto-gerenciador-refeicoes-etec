import pyqrcode
import png
import os

class QRCode:
    def func_gera_qrcodes(dados):
        for dado in dados:
            imagem = pyqrcode.create(dado)
            imagem.png(os.getcwd() + '/assets/dados/qr_code/' + dado +'.png',scale=5)

    def func_gera_qrcode(dado):
        imagem = pyqrcode.create(dado)
        endereco = os.getcwd() + '/assets/dados/qr_code/' + dado +'.png'
        imagem.png(endereco,scale=5)

        return endereco