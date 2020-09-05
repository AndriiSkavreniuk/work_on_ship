from flask_mail import Message
from app import mail
from config import Config


def send_email(order):
    msg = Message('Новий запит', recipients=Config.ADMINS)
    msg.body = order
    mail.send(msg)

