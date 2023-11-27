"""Схема для запроса list resource"""

schema = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "per_page": {"type": "number"},
        "total": {"type": "number"},
        "total_pages": {"type": "number"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "name": {"type": "string"},
                    "year": {"type": "number"},
                    "color": {"type": "string"},
                    "pantone_value": {"type": "string"},
                },
                "required": ["id", "name", "year", "color", "pantone_value"],
            },
        },
        "support": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "text": {"type": "string"}},
            "required": ["url", "text"],
        },
    },
}