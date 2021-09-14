update_schema = {
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
