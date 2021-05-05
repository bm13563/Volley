register_schema = {
    "type": "object",
    "properties": {
        "metadata": {
            "created": {"type": "string"},
        },
        "profile": {
            "name": {"type": "string"},
            "summary": {"type": "string"},
            "interests": [
                {"type": "string"},
                {"type": "string"},
            ],
            "score": {"type": "number"},
            "approximate_location": {
                "type": {"type": "string"},
                "coordinates": [
                    {"type": "number"},
                    {"type": "number"},
                ],
            },
        },
        "authentication": {
            "username": {"type": "string"},
            "password": {"type": "string"},
            "verified": {"type": "boolean"},
        },
        "events": {"type": "array"},
    },
}

register_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "summary": {"type": "string"},
        "interests": {"type": "array"},
        "approximate_location": {"type": "array"},
        "username": {"type": "string"},
        "password": {"type": "string"},
    },
}
