import json

from tests.base import set_up
from tests.test_utils import register, log_in, add_event
from tests.events.data.add import add_data


def test_json_does_not_match_schema():
    args = {"name": "a big test"}
    app, client = set_up()
    with client:
        response, args = register(client, args)
        assert response.status == "422 UNPROCESSABLE ENTITY"
        assert {
            "status": 422,
            "message": "Input JSON does not match shape/ types of schema",
        } == json.loads(response.data)


def test_json_types_do_not_match_schema():
    args = {
        "metadata": {"category": "litter"},
        "setting": {
            "event_start": "202104231600",
            "event_end": "202104231800",
            "location": "test",
        },
        "description": {
            "name": "My fun event!",
            "summary": "A really fun event - it's going to be really fun!",
            "social": "Omg let's go to the pub",
        },
        "parameters": {
            "max_attendance": 10,
            "documents": [
                "The first document description",
                "The second document description",
            ],
        },
    }
    app, client = set_up()
    with client:
        response, args = register(client, args)
        assert response.status == "422 UNPROCESSABLE ENTITY"
        assert {
            "status": 422,
            "message": "Input JSON does not match shape/ types of schema",
        } == json.loads(response.data)


def test_successful_add():
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        response, args = add_event(client)
        assert response.status == "200 OK"
        assert add_data == json.loads(response.data)

        # check that the event has been added to the user that created it
        response = client.get(
            "/users/user/60872f44eecdc50c62b0de96",
            follow_redirects=True,
        )
        assert response.status == "200 OK"
        assert (
            args["test_args"]["test_id"]
            in json.loads(response.data)["events"][0]["$oid"]
        )
