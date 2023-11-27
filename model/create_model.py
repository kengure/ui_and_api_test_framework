"""Модели для create user"""
from dataclasses import asdict, dataclass


@dataclass
class RequestCreateUserModel:
    """Класс для параметров request"""

    name: str
    job: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)


@dataclass
class ResponseCreateUserModel:
    """Класс для параметров response"""

    name: str
    job: str
    last_name: str
    id: str
    created_at: str
