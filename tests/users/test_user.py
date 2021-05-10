import json

from tests.base import set_up
from tests.test_utils import register
from tests.users.data.user import user_data


def test_successful_user():
    app, client = set_up()
    with client:
        register(client)
        response = client.get(
            "/users/user/60872f44eecdc50c62b0de96",
            follow_redirects=True,
        )
        assert response.status == "200 OK"
        assert user_data == json.loads(response.data)


def test_failed_user():
    app, client = set_up()
    with client:
        register(client)
        response = client.get(
            "/users/user/60872f44eecdc50c62b0de13",
            follow_redirects=True,
        )
        assert response.status == "404 NOT FOUND"
        assert {
            "status": 404,
            "message": "User does not exist",
        } == json.loads(response.data)
