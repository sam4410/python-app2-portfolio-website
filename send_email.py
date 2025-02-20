import smtplib
import ssl
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "sharma.manoj.aayush2303@gmail.com"
    password = os.environ.get("PASSWORD")
    receiver = "sharma.manoj.aayush2303@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
