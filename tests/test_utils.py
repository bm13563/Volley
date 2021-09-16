from tests.events.fixtures import events_new_user


def register(client, args=False):
    if not args:
        args = {
            "profile": {
                "name": "Big Benny M",
                "summary": "I like picking up litter",
                "interests": ["litter", "software"],
                "location": {
                    "coordinates": [-1.756465, 53.453474],
                },
            },
            "authentication": {
                "username": "bm13566@my.bristol.ac.uk",
                "password": "tuneful",
            },
            "test_args": {
                "test_id": "60872f44eecdc50c62b0de96",
                "test_date": "202104261000",
            },
        }
    return (
        client.post("/auth/register", json=args, follow_redirects=True),
        args,
    )


def log_in(client, args=False):
    if not args:
        args = {
            "authentication": {
                "username": "bm13566@my.bristol.ac.uk",
                "password": "tuneful",
            }
        }
    return client.post("/auth/log_in", json=args, follow_redirects=True), args


def log_out(client):
    return client.post("/auth/log_out", follow_redirects=True)


def add_event(client, args=False):
    if not args:
        args = {
            "metadata": {
                "category": "litter",
            },
            "setting": {
                "event_start": "202104231600",
                "event_end": "202104231800",
                "location": [-1.756465, 53.453474],
            },
            "description": {
                "name": "My fun event!",
                "summary": "A really fun event - it's going to be really fun!",
                "social": "Omg let's go to the pub",
            },
            "parameters": {
                "max_attendance": 10,
                "documents": [
                    "The first document description",
                    "The second document description",
                ],
                "attendance": {
                    "current_attendance": 0,
                    "attendees": [],
                },
            },
            "test_args": {
                "test_id": "60872f44eecdc50c62b0de96",
                "test_date": "202104261000",
            },
        }
    return client.post("/events/add", json=args, follow_redirects=True), args


def create_event_then_change_user(client):
    register(client)
    log_in(client)
    add_event(client)
    log_out(client)
    register(client, events_new_user)
    log_in(client, events_new_user)
