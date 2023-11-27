"""Схема для запроса register successful"""

schema = {
    "type": "object",
    "properties": {"id": {"type": "integer"}, "token": {"type": "string"}},
    "required": ["id", "token"],
}
