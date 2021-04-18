from tests.base import set_up, tear_down
from tests.authentication.test_registration import register
from tests.authentication.test_log_in import log_in


def log_out(client, args):
    return client.post("/auth/log_out", json=args, follow_redirects=True)


def test_successful_log_in():
    registration_args = {
        "name": "Big Benny M",
        "summary": "I like picking up litter",
        "interests": ["litter", "software"],
        "approximate_location": [-1.756465, 53.453474],
        "username": "bm13566@my.bristol.ac.uk",
        "password": "test_password1",
    }
    log_in_args = {
        "username": "bm13566@my.bristol.ac.uk",
        "password": "test_password1",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in(client, log_in_args)
        log_out_response = log_out(client, {})
        assert log_out_response.status == 200 or "200 OK"
        assert b"Successfully logged out!" in log_out_response.data
    tear_down()
