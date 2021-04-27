import json

from tests.base import set_up
from tests.utilities import register, log_in, add_event
from data.get import get_data


def test_successful_get():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        add_event(client)
        get_response = client.post(
            "/events/get/60872f44eecdc50c62b0de96",
            follow_redirects=True,
        )
        assert get_response.status == 200 or "200 OK"
        assert get_data == json.loads(get_response.data)
