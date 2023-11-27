"""Схема для запроса list users"""

schema = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"},
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"],
            },
        },
        "support": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "text": {"type": "string"}},
            "required": ["url", "text"],
        },
    },
}
