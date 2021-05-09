from tests.base import set_up
from tests.test_utils import register, log_in


def test_successful_log_out():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        response = client.post("/auth/log_out", follow_redirects=True)
        assert response.status == "200 OK"
        assert b"Successfully logged out!" == response.data
