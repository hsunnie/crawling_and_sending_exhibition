import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders
from os.path import basename
import os

# 현재 경로
file_path = os.path.dirname(os.path.realpath(__file__))

# 서버 및 이메일 보내는 사람의 정보
SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 465
SMTP_USER = open(str(file_path) + '\\naverid.txt').read().strip() +'@naver.com'
SMTP_PW = open(str(file_path) + '\\naverpw.txt').read().strip()

def send_email(subject, content=''):
    """
    subject: 제목 (str)
    content: 내용 (str) [Optional]
    """
    msg = MIMEMultipart('alternative')

    msg['From'] = SMTP_USER
    msg['To'] = SMTP_USER
    msg['Subject'] = subject

    text = MIMEText(content, 'html')

    msg.attach(text)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PW)
    smtp.sendmail(SMTP_USER, SMTP_USER, msg.as_string())
    smtp.close()