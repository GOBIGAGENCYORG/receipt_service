import logging

from settings import settings


class Logger:
    _logger: logging.Logger | None = None
    _default_logger_name = "logger"
    _default_handler_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    @classmethod
    def get_logger(cls, name: str | None = None) -> logging.Logger:
        if not cls._logger:
            return cls._init_logger(name)
        return cls._logger

    @classmethod
    def get_default_handler(cls, format: str | None = None):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(settings.logging_level)

        formatter = logging.Formatter(format or cls._default_handler_format)
        console_handler.setFormatter(formatter)
        return console_handler

    @classmethod
    def _init_logger(cls, name: str | None = None):
        cls._logger = logging.getLogger(name or "logger")
        cls._logger.setLevel(settings.logging_level)
        cls._logger.addHandler(cls.get_default_handler())
        return cls._logger


class LoggingProvider:

    def __init__(self):
        self._logger = Logger.get_logger(name=self.__class__.__name__)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.debug(message)

    def warning(self, message: str):
        self._logger.debug(message)

    def error(self, message: str):
        self._logger.debug(message)

    def critical(self, message: str):
        self._logger.debug(message)

    def exception(self, exception: Exception):
        self._logger.exception(exception)
