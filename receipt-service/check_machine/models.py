import pydantic
import datetime


class ReceiptDataModel(pydantic.BaseModel):
    identity: str
    datetime: datetime.datetime
    products: list[str]
    price: str
    discount: str
    email: str
    subject: str
    text: str
