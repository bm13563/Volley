log_in_schema = {
    "authentication": {
        "username": str,
        "password": str,
    }
}

register_schema = {
    "profile": {
        "name": str,
        "summary": str,
        "interests": list,
        "location": {
            "coordinates": list,
        },
    },
    "authentication": {
        "username": str,
        "password": str,
    },
}
