"""Модели для register"""
from dataclasses import asdict, dataclass


@dataclass
class RequestRegisterSuccessfulModel:
    """Класс для параметров request"""

    email: str
    password: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)


@dataclass
class RequestRegisterUnsuccessfulModel:
    """Класс для параметров request"""

    email: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)


@dataclass
class ResponseRegisterModel:
    """Класс для параметров response"""

    id: int
    token: str
