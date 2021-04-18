from api.models.users import User


def register(client, registration_args):
    return client.post(
        "/auth/register", json=registration_args, follow_redirects=True
    )


def log_in(client, args):
    return client.post("/auth/log_in", json=args, follow_redirects=True)


def register_and_log_in(client):
    registration_args = {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "approximate_location": [-1.756465, 53.453474],
        "username": "bm13566@my.bristol.ac.uk",
        "password": "test_password1",
    }
    log_in_args = {
        "username": "bm13566@my.bristol.ac.uk",
        "password": "test_password1",
    }
    register(client, registration_args)
    log_in(client, log_in_args)
    return User.objects(authentication__username=registration_args["username"])
