"""Модель respons-а для single resource"""
from dataclasses import dataclass


@dataclass
class ResponseSingleResourceModel:
    """Класс для параметров response"""

    id: int
    name: str
    year: int
    color: str
    pantone_value: str
