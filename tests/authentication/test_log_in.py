from tests.base import set_up, tear_down
from tests.utilities import register, log_in


def test_successful_log_in():
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
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in_response = log_in(client, log_in_args)
        assert log_in_response.status == 200 or "200 OK"
        assert b"Successfully logged in!" in log_in_response.data
    tear_down()


def test_incorrect_password():
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
        "password": "test_password6",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in_response = log_in(client, log_in_args)
        assert log_in_response.status == 200 or "200 OK"
        assert b"Incorrect password" in log_in_response.data
    tear_down()


def test_incorrect_username():
    registration_args = {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "approximate_location": [-1.756465, 53.453474],
        "username": "bm13566@my.bristol.ac.uk",
        "password": "test_password1",
    }
    log_in_args = {
        "username": "bm13569@my.bristol.ac.uk",
        "password": "test_password6",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in_response = log_in(client, log_in_args)
        assert log_in_response.status == 200 or "200 OK"
        assert b"User does not exist" in log_in_response.data
    tear_down()
