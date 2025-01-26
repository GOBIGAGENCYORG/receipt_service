# TODO: Refactor

import json
import os

from settings import settings
from check_machine.models import ReceiptDataModel
from check_machine.service import CheckMachine
from mail_service.service import MailService
from receipt_counter.service import ReceiptCounter
from ftp.service import FTPLoader


def message_callback(channel, method, properties, body):
    parsed_message = ReceiptDataModel(**eval(json.loads(body)))
    document_no = ReceiptCounter().get()
    filename = f"{document_no}_{parsed_message.identity}_{int(parsed_message.datetime.timestamp())}.jpg"
    CheckMachine(
        datetime=parsed_message.datetime,
        products=parsed_message.products,
        price=parsed_message.price,
        discount=parsed_message.discount,
        document_no=document_no,
        email=parsed_message.email,
        filename=filename,
    ).make_receipt()
    MailService().send(
        sender=settings.email_address,
        recipient=parsed_message.email,
        text=parsed_message.text,
        subject=parsed_message.subject,
        image_filename=filename,
    )
    FTPLoader().send_file_to_ftp(filename)
    os.remove(filename)
    channel.basic_ack(delivery_tag=method.delivery_tag)
