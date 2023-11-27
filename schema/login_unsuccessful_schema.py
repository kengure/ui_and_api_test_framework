"""Схема для запроса login unsuccessful"""

schema = {
    "type": "object",
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}
