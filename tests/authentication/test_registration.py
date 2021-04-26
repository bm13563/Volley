import json

from tests.base import set_up
from tests.utilities import register
from data.registration import registration_data


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
