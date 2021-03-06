events_add_data = {
    "_id": {"$oid": "60872f44eecdc50c62b0de96"},
    "metadata": {
        "metadata_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "created": {"$date": 1619431200000},
        "owner": {"$oid": "60872f44eecdc50c62b0de96"},
        "category": "litter",
    },
    "status": {
        "status_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "finished": False,
        "ongoing": False,
        "full": False,
        "cancelled": False,
    },
    "setting": {
        "setting_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "event_start": {"$date": 1619193600000},
        "event_end": {"$date": 1619200800000},
        "location": {"type": "Point", "coordinates": [-1.756465, 53.453474]},
    },
    "description": {
        "description_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "name": "My fun event!",
        "summary": "A really fun event - it's going to be really fun!",
        "social": "Omg let's go to the pub",
    },
    "parameters": {
        "parameters_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "max_attendance": 10,
        "approval_required": False,
        "documents_required": False,
        "documents": [
            {
                "document_id": {"$oid": "60872f44eecdc50c62b0de96"},
                "explanation": "The first document description",
            },
            {
                "document_id": {"$oid": "60872f44eecdc50c62b0de96"},
                "explanation": "The second document description",
            },
        ],
        "attendance": {
            "attendance_id": {"$oid": "60872f44eecdc50c62b0de96"},
            "current_attendance": 0,
            "attendees": [],
        },
    },
}

events_get_data = {
    "_id": {"$oid": "60872f44eecdc50c62b0de96"},
    "metadata": {
        "metadata_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "created": {"$date": 1619431200000},
        "owner": {"$oid": "60872f44eecdc50c62b0de96"},
        "category": "litter",
    },
    "status": {
        "status_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "finished": False,
        "ongoing": False,
        "full": False,
        "cancelled": False,
    },
    "setting": {
        "setting_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "event_start": {"$date": 1619193600000},
        "event_end": {"$date": 1619200800000},
        "location": {"type": "Point", "coordinates": [-1.756465, 53.453474]},
    },
    "description": {
        "description_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "name": "My fun event!",
        "summary": "A really fun event - it's going to be really fun!",
        "social": "Omg let's go to the pub",
    },
    "parameters": {
        "parameters_id": {"$oid": "60872f44eecdc50c62b0de96"},
        "max_attendance": 10,
        "approval_required": False,
        "documents_required": False,
        "documents": [
            {
                "document_id": {"$oid": "60872f44eecdc50c62b0de96"},
                "explanation": "The first document description",
            },
            {
                "document_id": {"$oid": "60872f44eecdc50c62b0de96"},
                "explanation": "The second document description",
            },
        ],
        "attendance": {
            "attendance_id": {"$oid": "60872f44eecdc50c62b0de96"},
            "current_attendance": 0,
            "attendees": [],
        },
    },
}

events_new_user = {
    "profile": {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "location": {
            "coordinates": [-1.756465, 53.453474],
        },
    },
    "authentication": {
        "username": "bm13565@my.bristol.ac.uk",
        "password": "tuneful2",
    },
    "test_args": {
        "test_id": "60872f44eecdc50c62b0de98",
        "test_date": "202104261000",
    },
}
