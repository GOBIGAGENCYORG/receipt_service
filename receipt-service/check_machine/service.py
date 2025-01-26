import cv2
import numpy
import numpy as np
import datetime
from PIL import ImageFont, Image, ImageDraw

IMG = cv2.imread("static/base_receipt.jpg")


class CheckMachine:
    def __init__(
        self,
        datetime: datetime.datetime,
        products: list[str],
        price: str,
        discount: str,
        filename: str,
        document_no: int,
        email: str,
    ):
        self.default_x = 710
        self.filename = filename

        self.document_name_pos = [self.default_x, 685]
        self.document_name = "Документ о расчётах"
        self.date_pos = [self.default_x, 840]
        self.date = datetime.strftime("%d.%m.%Y ; %H:%M")
        self.site_pos = [self.default_x, 890]
        self.site = "gobig-agency.com"

        self.seller_info_name_pos = [self.default_x, 1050]
        self.seller_info_name = "Блинкова Анастасия Александровна"
        self.seller_info_inn_pos = [self.default_x, 1100]
        self.seller_info_inn = "572007138923"

        self.nalog_sys_pos = [self.default_x, 1255]
        self.nalog_sys = "Патентная система налогообложения"

        self.type_pos = [self.default_x, 1430]
        self.type = "Приход"

        self.products = products
        self.products_len = len(self.products)
        self.product_pos = [self.default_x, 1590]
        self.height_additional_products = 1625
        self.height2_additional_products = 1655
        self.counter = 0

        self.amount = str(len(self.products))
        self.amount_pos = [self.default_x, 1675]

        self.price_pos = [self.default_x, 1745]
        self.price = price + " RUB"

        self.discount_pos = [self.default_x, 1815]
        self.discount = discount

        self.raschetsum_pos = [self.default_x, 1965]
        self.raschetsum = self.price

        self.raschetform_pos = [self.default_x, 2145]
        self.raschetform = "Рассрочка"

        self.oplatasum_pos = [self.default_x, 2310]
        self.oplatasum = self.price

        self.client_mail_pos = [self.default_x, 2480]
        self.client_mail = email

        self.doljnostfio1_pos = [self.default_x, 2650]
        self.doljnostfio1 = "ИП Блинкова Анастасия"
        self.doljnostfio2_pos = [self.default_x, 2700]
        self.doljnostfio2 = "Александровна"

        self.ip_mail_pos = [self.default_x, 2850]
        self.ip_mail = "anastasia_blinkova1@mail.ru"

        self.document_no_pos = [self.default_x + 500, 3300]
        num = list(str(document_no))
        self.document_no = list("000000000")
        for i in range(len(num)):
            self.document_no[-i - 1] = num[-i - 1]
        self.document_no = "".join(self.document_no)

    def update_heights(self, height):
        padding = 7
        self.amount_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.price_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.discount_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.raschetsum_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.raschetform_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.oplatasum_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.doljnostfio1_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.doljnostfio2_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.ip_mail_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )
        self.client_mail_pos[1] += (
            height - (self.products_len - len(self.products)) * 2 - padding
        )

    def make_receipt(self):
        img = IMG.copy()
        fontpath = "static/Montserrat-Light.ttf"
        font = ImageFont.truetype(fontpath, 30)
        if len(self.products) != 1:
            first_half = img[0 : self.height_additional_products, :]
            second_half = img[self.height2_additional_products :, :]
            for i in range(len(self.products)):
                newline = img[
                    self.height_additional_products : self.height2_additional_products,
                    :,
                ]
                self.counter += 1
                first_half = numpy.append(first_half, newline).reshape(-1, 1496, 3)
                self.update_heights(newline.shape[0] - 6)
            img = numpy.append(first_half, second_half).reshape(-1, 1496, 3)

        image = Image.fromarray(img)
        draw = ImageDraw.Draw(image)
        draw.text(
            (self.document_name_pos[0], self.document_name_pos[1]),
            self.document_name,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.date_pos[0], self.date_pos[1]),
            self.date,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.site_pos[0], self.site_pos[1]),
            self.site,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.seller_info_name_pos[0], self.seller_info_name_pos[1]),
            self.seller_info_name,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.seller_info_inn_pos[0], self.seller_info_inn_pos[1]),
            self.seller_info_inn,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.nalog_sys_pos[0], self.nalog_sys_pos[1]),
            self.nalog_sys,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.type_pos[0], self.type_pos[1]),
            self.type,
            font=font,
            fill=(0, 0, 0, 1),
        )
        if len(self.products) == 1:
            draw.text(
                (self.product_pos[0], self.product_pos[1]),
                self.products[0],
                font=font,
                fill=(0, 0, 0, 1),
            )
        else:
            for i in range(self.counter):
                if len(self.products) == 0:
                    break
                draw.text(
                    (self.product_pos[0], self.product_pos[1]),
                    self.products.pop(0),
                    font=font,
                    fill=(0, 0, 0, 1),
                )
                self.product_pos[1] += 40
        draw.text(
            (self.amount_pos[0], self.amount_pos[1]),
            self.amount,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.price_pos[0], self.price_pos[1]),
            self.price,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.discount_pos[0], self.discount_pos[1]),
            self.discount,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.raschetsum_pos[0], self.raschetsum_pos[1]),
            self.raschetsum,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.raschetform_pos[0], self.raschetform_pos[1]),
            self.raschetform,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.oplatasum_pos[0], self.oplatasum_pos[1]),
            self.oplatasum,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.client_mail_pos[0], self.client_mail_pos[1]),
            self.client_mail,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.doljnostfio1_pos[0], self.doljnostfio1_pos[1]),
            self.doljnostfio1,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.doljnostfio2_pos[0], self.doljnostfio2_pos[1]),
            self.doljnostfio2,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.ip_mail_pos[0], self.ip_mail_pos[1]),
            self.ip_mail,
            font=font,
            fill=(0, 0, 0, 1),
        )
        draw.text(
            (self.document_no_pos[0], self.document_no_pos[1]),
            self.document_no,
            font=font,
            fill=(0, 0, 0, 1),
        )

        img = np.array(image)
        print(self.filename)
        cv2.imwrite(self.filename, img)
