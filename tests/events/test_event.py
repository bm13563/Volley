import json

from tests.base import set_up
from tests.test_utils import register, log_in, add_event
from data.get import get_data


def test_successful_get():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        add_event(client)
        get_response = client.get(
            "/events/event/60872f44eecdc50c62b0de96",
            follow_redirects=True,
        )
        assert get_response.status == "200 OK"
        assert get_data == json.loads(get_response.data)


def test_failed_get():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        add_event(client)
        get_response = client.get(
            "/events/event/60872f44eecdc50c62b0de98",
            follow_redirects=True,
        )
        assert get_response.status == "200 OK"
        assert b"This event does not exist" in get_response.data
