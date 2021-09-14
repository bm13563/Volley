import json

from tests.base import set_up
from tests.test_utils import register, log_in
from tests.users.fixtures import users_update_data


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
        "profile": {
            "name": 22,
            "summary": "I like picking up litter",
            "interests": ["litter", "software"],
            "location": {
                "coordinates": [-1.756465, 53.453474],
            },
        },
        "authentication": {
            "username": "bm13566@my.bristol.ac.uk",
            "password": "tuneful",
        },
        "test_args": {
            "test_id": "60872f44eecdc50c62b0de96",
            "test_date": "202104261000",
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


def test_successful_summary_update():
    args = {
        "profile": {
            "name": "Big Benny M",
            "summary": "A huge change to the summary",
            "interests": ["litter", "software"],
            "location": {
                "coordinates": [-1.756465, 53.453474],
            },
        },
        "authentication": {
            "username": "bm13566@my.bristol.ac.uk",
            "password": "tuneful",
        },
        "test_args": {
            "test_id": "60872f44eecdc50c62b0de96",
            "test_date": "202104261000",
        },
    }
    app, client = set_up()
    with client:
        register(client)
        log_in(client)
        response = client.post(
            "/users/update",
            json=args,
            follow_redirects=True,
        )
        assert response.status == "200 OK"
        assert users_update_data == json.loads(response.data)
