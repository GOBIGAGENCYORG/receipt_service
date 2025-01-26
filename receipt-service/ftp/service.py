# TODO: Refactor

import os
from ftplib import FTP
from datetime import datetime
from logger import LoggingProvider
from settings import settings


class FTPLoader(LoggingProvider):
    ftp: FTP

    def __init__(self):
        super().__init__()
        self.debug("Initializing")
        self.address: str = settings.ftp_host
        self.username: str = settings.ftp_username
        self.password: str = settings.ftp_password
        self.connect()
        self.working: bool = True
        self.debug("Initialized")

    def connect(self):
        self.debug("Trying to connect to ftp")
        self.ftp = FTP(self.address)
        self.ftp.login(self.username, self.password)
        self.debug("Connected")

    def disconnect(self):
        self.ftp.close()
        self.debug("Disconnected")

    def chdir(self, directory: str):
        if self.directory_exists(directory) is False:
            self.debug("Creating directory")
            self.ftp.mkd(directory)
        self.ftp.cwd(directory)

    def directory_exists(self, directory: str):
        files_list = []
        self.ftp.retrlines("LIST", files_list.append)
        for f in files_list:
            if f.split()[-1] == directory and f.upper().startswith("D"):
                return True
        return False

    def ftp_upload(self, file, file_type="img"):
        if file_type == "TXT":
            with open(file) as file_object:
                self.ftp.storlines("STOR " + file, file_object)
        else:
            with open(file, "rb") as file_object:
                self.ftp.storbinary(f"STOR {file}", file_object)

    def send_file_to_ftp(self, file_path: str):
        self.info(f"Uploading {file_path} to ftp")
        self.connect()
        self.chdir(str(datetime.now().year))
        self.chdir(str(datetime.now().month))
        self.chdir(str(datetime.now().day))
        self.ftp_upload(file_path, file_type="img")
        status = None
        if file_path in self.ftp.nlst():
            self.info("File uploaded")
            status = True
        else:
            self.error("File is not uploaded")
        self.ftp.cwd("/")
        self.disconnect()
        return status
