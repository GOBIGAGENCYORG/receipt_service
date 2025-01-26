from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Literal

ValidLoggingLevels = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    rabbitmq_host: str = Field(..., alias="RABBITMQ_HOST")
    logging_level: ValidLoggingLevels = Field(..., alias="LOGGING_LEVEL")
    email_address: str = Field(..., alias="SERVICE_EMAIL_ADDRESS")
    email_smtp_address: str = Field(..., alias="EMAIL_SMTP_ADDRESS")
    email_smtp_port: int = Field(..., alias="EMAIL_SMTP_PORT")
    ftp_host: str = Field(..., alias="FTP_HOST")
    ftp_username: str = Field(..., alias="FTP_USERNAME")
    receipts_rabbit_queue: str = Field(..., alias="RECEIPTS_RABBIT_QUEUE")
    ftp_password: str = Field(..., alias="FTP_PASSWORD")
    email_token: str = Field(..., alias="EMAIL_TOKEN")


settings = Settings()
