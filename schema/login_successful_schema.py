"""Схема для запроса login successful"""

schema = {
    "type": "object",
    "properties": {"token": {"type": "string"}},
    "required": ["token"],
}
