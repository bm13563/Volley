import json

from tests.base import set_up
from tests.test_utils import (
    create_event_then_change_user,
    register,
    log_in,
    add_event,
)
from tests.events.fixtures import events_get_data


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
        assert events_get_data == json.loads(response.data)


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
        assert {
            "status": 404,
            "message": "Event does not exist",
        } == json.loads(response.data)


def test_permission_denied_event():
    app, client = set_up()
    with client:
        create_event_then_change_user(client)
        response = client.get(
            "/events/event/60872f44eecdc50c62b0de96",
            follow_redirects=True,
        )
        assert response.status == "403 FORBIDDEN"
        assert {
            "status": 403,
            "message": "You do not have permission to view this event",
        } == json.loads(response.data)
