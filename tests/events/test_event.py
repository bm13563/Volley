import json

from tests.base import set_up
from tests.test_utils import register, log_in, add_event
from data.event import event_data


def test_successful_event():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        add_event(client)
        response = client.get(
            "/events/event/60872f44eecdc50c62b0de96",
            follow_redirects=True,
        )
        assert response.status == "200 OK"
        assert event_data == json.loads(response.data)


def test_failed_event():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        add_event(client)
        response = client.get(
            "/events/event/60872f44eecdc50c62b0de98",
            follow_redirects=True,
        )
        assert response.status == "404 NOT FOUND"
        assert b"Event does not exist" in response.data
