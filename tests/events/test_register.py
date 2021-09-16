from tests.base import set_up
from tests.test_utils import (
    create_event_then_change_user,
)


def test_successful_register():
    args = {
        "event_id": "60872f44eecdc50c62b0de96",
    }
    app, client = set_up()
    with client:
        create_event_then_change_user(client)
        response = client.post(
            "/events/register",
            json=args,
            follow_redirects=True,
        )
        assert response.status == "200 OK"
