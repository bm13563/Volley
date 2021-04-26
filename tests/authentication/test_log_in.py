import json

from tests.base import set_up
from tests.utilities import register, log_in
from data.log_in import log_in_data


def test_successful_log_in():
    app, client = set_up()
    with client:
        register(client)
        log_in_response, args = log_in(client)
        assert log_in_response.status == 200 or "200 OK"
        assert log_in_data == json.loads(log_in_response.data)


def test_incorrect_password():
    registration_args = {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "approximate_location": [-1.756465, 53.453474],
        "username": "bm13566@my.bristol.ac.uk",
        "password": "tuneful",
        "test_args": {
            "test_id": "60872f44eecdc50c62b0de96",
            "test_date": "202104261000",
            "test_password": "tuneful",
        },
    }
    log_in_args = {
        "username": "bm13566@my.bristol.ac.uk",
        "password": "really tuneless",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in_response, args = log_in(client, log_in_args)
        assert log_in_response.status == 200 or "200 OK"
        assert b"Incorrect password" in log_in_response.data


def test_incorrect_username():
    registration_args = {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "approximate_location": [-1.756465, 53.453474],
        "username": "bm13566@my.bristol.ac.uk",
        "password": "tuneful",
        "test_args": {
            "test_id": "60872f44eecdc50c62b0de96",
            "test_date": "202104261000",
            "test_password": "tuneful",
        },
    }
    log_in_args = {
        "username": "tuneless@my.bristol.ac.uk",
        "password": "really tuneless",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in_response, args = log_in(client, log_in_args)
        assert log_in_response.status == 200 or "200 OK"
        assert b"User does not exist" in log_in_response.data
