import os
import smtplib
from email.message import EmailMessage
import imghdr

# autorizacoes
EMAIL_GMAIL =  ''
SENHA_GMAIL = ''
SMTP_GMAIL = "smtp.gmail.com: 587"

EMAIL_OUTLOOK = ''
SENHA_OUTLOOK = ''
SMTP_OUTLOOK = "smtp.office365.com: 587"

# conteudo
CORPO = """
<p>ETEC CIDADE TIRADENTES - 199</p>
<p>
Prezado(a) ALUNO(a), 
<br><br>
O gerenciamento de refeições servidas pela cantina sera administrado por QR CODE, 
sendo baseado no E-mail Institucional(concedido a todos os aluno do Centro Paula Souza). 
O procedimento sera consistido na apresentação do QR CODE ao leitor disponível na cantina, 
para poder deleitar-se da refeição. 
<br><br>
<b>Recomendação:</b> Mantenha resguardado seus dados de acesso ao E-mail Institucional e preserve este QR CODE.
<br><br>
Atenciosamente,
<br><br>
Kaique Souza Santos
<br>
Desenvolvedor do Sistema
</p>
"""

ASSUNTO = "ETEC CIDADE TIRADENTES - 199 - ACESSO PARA CANTINA"

class Email:
    def envia_email(destinatario, imagem):
        mensagem = EmailMessage()
        mensagem['Subject'] = ASSUNTO
        mensagem['To'] = destinatario 
        mensagem.add_header('Content-Type', 'text/html')
        mensagem.set_payload(CORPO)

        with open(os.getcwd() + '/assets/dados/qr_code/' + imagem +'.png', 'rb') as imagem_read:
            file_data = imagem_read.read()
            file_type = imghdr.what(imagem_read.name)
            file_name = imagem + '.png'

        mensagem.add_attachment(
            file_data, 
            maintype = 'image', 
            subtype = file_type,
            filename = file_name
        )

        if(Email.func_smtp(mensagem, EMAIL_OUTLOOK, SENHA_OUTLOOK, destinatario, SMTP_OUTLOOK) == False):
            Email.func_smtp(mensagem, EMAIL_GMAIL, SENHA_GMAIL, destinatario, SMTP_GMAIL)
                
    def func_smtp(mensagem, email, senha, destinatario, smtp):
        try:
            mensagem['From'] = email    
            server = smtplib.SMTP(smtp)
            server.starttls()
        
            server.login(email, senha)
            server.sendmail(email, [destinatario], mensagem.as_string().encode('utf-8'))
            return True
        except:
            return False
