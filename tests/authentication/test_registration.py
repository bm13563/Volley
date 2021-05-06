import json

from tests.base import set_up
from tests.test_utils import register
from data.registration import registration_data


def test_json_does_not_match_schema():
    args = {"name": "a big test"}
    app, client = set_up()
    with client:
        register_response, args = register(client, args)
        assert register_response.status == 200 or "200 OK"
        assert (
            b"Input JSON does not match shape/ types of schema"
            in register_response.data
        )


def test_json_types_do_not_match_schema():
    args = {
        "profile": {
            "name": 22,
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
    app, client = set_up()
    with client:
        register_response, args = register(client, args)
        assert register_response.status == 200 or "200 OK"
        assert (
            b"Input JSON does not match shape/ types of schema"
            in register_response.data
        )


def test_successful_registration():
    app, client = set_up()
    with client:
        register_response, args = register(client)
        assert register_response.status == 200 or "200 OK"
        assert registration_data == json.loads(register_response.data)


def test_user_exists():
    app, client = set_up()
    with client:
        register(client)
        register_response, args = register(client)
        assert register_response.status == 200 or "200 OK"
        assert (
            b"An account already exists with this username, sorry"
            in register_response.data
        )
