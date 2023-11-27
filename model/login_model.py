"""Модели для login"""
from dataclasses import asdict, dataclass


@dataclass
class RequestLoginSuccessfulModel:
    """Класс для параметров request"""

    email: str
    password: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)


@dataclass
class RequestLoginUnsuccessfulModel:
    """Класс для параметров request"""

    email: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)


@dataclass
class ResponseLoginrModel:
    """Класс для параметров response"""

    token: str
