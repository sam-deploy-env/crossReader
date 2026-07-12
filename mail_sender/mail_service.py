from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os

from constants import mail_data, file_data
from config import config

def send_mail():
    message = MIMEMultipart()
    message['FROM'] = mail_data.MAIL_FROM
    message['TO'] = mail_data.MAIL_TO
    message['SUBJECT'] = mail_data.MAIL_SUBJECT
    message.attach(MIMEText(mail_data.MAIL_BODY, 'plain'))
    attachment_path = file_data.FINAL_WORD_FILENAME
    filename = os.path.basename(attachment_path)
    with open(attachment_path, 'rb') as attachment :
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    message.attach(part)
    try:
        with smtplib.SMTP_SSL(mail_data.SMTP, mail_data.PORT) as server:
            server.login(mail_data.MAIL_FROM, config.MAIL_PASSWORD)
            server.send_message(message)
    except Exception as e:
        print(f"Erreur lors de l'envoi du mail : {e}")