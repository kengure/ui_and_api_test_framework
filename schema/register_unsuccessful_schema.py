"""Схема для запроса register unsuccessful"""

schema = {
    "type": "object",
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}
