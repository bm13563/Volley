import json

from tests.base import set_up
from tests.utilities import register, log_in, add_event
from data.add import add_data


def test_successful_add():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        add_response, args = add_event(client)
        assert add_response.status == 200 or "200 OK"
        assert add_data == json.loads(add_response.data)
