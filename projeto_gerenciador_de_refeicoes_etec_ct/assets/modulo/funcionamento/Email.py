import os
import smtplib
from email.message import EmailMessage
import imghdr

# autorizacoes

EMAIL = 'kaiquesouzasantos90@gmail.com'
SENHA = 'hepyyzzcecisgpgn'
SMTP = "smtp.gmail.com: 587"

# conteudo
CORPO = """
<p>ETEC CIDADE TIRADENTES - 199</p>
<p>Segue </p>
"""

ASSUNTO = "ETEC CIDADE TIRADENTES - 199 - ACESSO PARA CANTINA"

class Email:
    def envia_email(destinatario, imagem):
        mensagem = EmailMessage()

        mensagem['Subject'] = ASSUNTO
        mensagem['From'] = EMAIL
        mensagem['To'] = destinatario 

        mensagem.add_header('Content-Type', 'text/html')
        mensagem.set_payload(CORPO)

        with open(os.getcwd() + '/assets/dados/qr_code/' + imagem +'.png', 'rb') as imagem_read:
            file_data = imagem_read.read()
            file_type = imghdr.what(imagem_read.name)
            file_name = imagem_read.name

        mensagem.add_attachment(
            file_data, 
            maintype = 'image', 
            subtype = file_type,
            filename = file_name
        )
            
        server = smtplib.SMTP(SMTP)
        server.starttls()
        
        server.login(EMAIL, SENHA)
        server.sendmail(EMAIL, [destinatario], mensagem.as_string().encode('utf-8'))
        print('Email enviado')