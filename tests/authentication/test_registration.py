from tests.base import set_up, tear_down
from tests.utilities import register


def test_successful_registration():
    registration_args = {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "approximate_location": [-1.756465, 53.453474],
        "username": "bm13566@my.bristol.ac.uk",
        "password": "test_password1",
    }
    app, client = set_up()
    with client:
        register_response = register(client, registration_args)
        assert register_response.status == 200 or "200 OK"
        assert b"successfully added user" in register_response.data
    tear_down()


def test_user_exists():
    registration_args = {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "approximate_location": [-1.756465, 53.453474],
        "username": "bm13566@my.bristol.ac.uk",
        "password": "test_password1",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        register_response = register(client, registration_args)
        assert register_response.status == 200 or "200 OK"
        assert (
            b"An account already exists with this username, sorry"
            in register_response.data
        )
    tear_down()
