# from api.models.users import User, Event
from .base import base_data


def register(client, args=False):
    if not args:
        args = {
            "name": "Big Benny M",
            "summary": "I like picking up litter",
            "interests": ["litter", "software"],
            "approximate_location": [-1.756465, 53.453474],
            "username": "bm13566@my.bristol.ac.uk",
            "password": "tuneful",
            "test_args": base_data,
        }
    return (
        client.post("/auth/register", json=args, follow_redirects=True),
        args,
    )


def log_in(client, args=False):
    if not args:
        args = {
            "username": "bm13566@my.bristol.ac.uk",
            "password": "tuneful",
            "test_args": base_data,
        }
    return client.post("/auth/log_in", json=args, follow_redirects=True), args
