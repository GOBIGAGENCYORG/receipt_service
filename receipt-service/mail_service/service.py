import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from settings import settings


class MailService:

    def __init__(self):
        self._smtp_conn = smtplib.SMTP_SSL(
            settings.email_smtp_address, settings.email_smtp_port
        )
        self._login(settings.email_address, settings.email_token)

    def _check_conn(self):
        self._smtp_conn.ehlo()

    def _login(self, login, password):
        self._smtp_conn.login(login, password)

    def _build_message(
        sender: str, recipient: str, message: str | None, subject: str
    ) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient
        return msg

    def send(
        self,
        sender: str,
        recipient: str,
        text: str,
        subject: str,
        image_filename: str | None,
    ):
        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = sender
        message["To"] = recipient
        print(text)
        message.attach(MIMEText(text))
        if image_filename:
            with open(image_filename, "rb") as image_file:
                message.attach(
                    MIMEImage(image_file.read(), name=os.path.basename(image_filename))
                )
        self._smtp_conn.sendmail(sender, recipient, message.as_string())
