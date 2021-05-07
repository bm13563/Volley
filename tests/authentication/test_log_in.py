import json

from tests.base import set_up
from tests.test_utils import register, log_in
from data.log_in import log_in_data


def test_json_does_not_match_schema():
    args = {"name": "a big test"}
    app, client = set_up()
    with client:
        register(client)
        log_in_response, args = log_in(client, args)
        assert log_in_response.status == "422 UNPROCESSABLE ENTITY"
        assert {
            "status": 422,
            "message": "Input JSON does not match shape/ types of schema",
        } == json.loads(log_in_response.data)


def test_json_types_do_not_match_schema():
    args = {
        "username": 25,
        "password": "tuneful",
    }
    app, client = set_up()
    with client:
        register(client)
        log_in_response, args = log_in(client, args)
        assert log_in_response.status == "422 UNPROCESSABLE ENTITY"
        assert {
            "status": 422,
            "message": "Input JSON does not match shape/ types of schema",
        } == json.loads(log_in_response.data)


def test_successful_log_in():
    app, client = set_up()
    with client:
        register(client)
        log_in_response, args = log_in(client)
        assert log_in_response.status == "200 OK"
        assert log_in_data == json.loads(log_in_response.data)


def test_incorrect_password():
    registration_args = {
        "profile": {
            "name": "Big Benny M",
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
    log_in_args = {
        "username": "bm13566@my.bristol.ac.uk",
        "password": "really tuneless",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in_response, args = log_in(client, log_in_args)
        assert log_in_response.status == "403 FORBIDDEN"
        assert {
            "status": 403,
            "message": "Incorrect password",
        } == json.loads(log_in_response.data)


def test_incorrect_username():
    registration_args = {
        "profile": {
            "name": "Big Benny M",
            "summary": "I like picking up litter",
            "interests": ["litter", "software"],
            "location": {
                "coordinates": [-1.756465, 53.453474],
            },
        },
        "authentication": {
            "username": "bm13563@my.bristol.ac.uk",
            "password": "test_password1",
        },
    }
    log_in_args = {
        "username": "tuneless@my.bristol.ac.uk",
        "password": "really tuneless",
    }
    app, client = set_up()
    with client:
        register(client, registration_args)
        log_in_response, args = log_in(client, log_in_args)
        assert log_in_response.status == "404 NOT FOUND"
        assert {
            "status": 404,
            "message": "User does not exist",
        } == json.loads(log_in_response.data)
