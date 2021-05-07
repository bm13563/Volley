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


def add_event(client, args=False):
    if not args:
        args = {
            "category": "litter",
            "event_start": "202104231600",
            "event_end": "202104231800",
            "location": [-1.756465, 53.453474],
            "name": "My fun event!",
            "summary": "A really fun event - it's going to be really fun!",
            "social": "Omg let's go to the pub",
            "max_attendance": 10,
            "explanations": [
                "The first document description",
                "The second document description",
            ],
            "test_args": {
                "test_id": "60872f44eecdc50c62b0de96",
                "test_date": "202104261000",
            },
        }
    return client.post("/events/add", json=args, follow_redirects=True), args
