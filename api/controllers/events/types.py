events_add_schema = {
    "metadata": {
        "category": str,
    },
    "setting": {
        "event_start": str,
        "event_end": str,
        "location": list,
    },
    "description": {
        "name": str,
        "summary": str,
        "social": str,
    },
    "parameters": {
        "max_attendance": int,
        "documents": list,
        "attendance": {"current_attendance": int, "attendees": list},
    },
}

events_register_schema = {
    "event_id": str,
}
