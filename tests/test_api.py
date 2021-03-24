import pytest, tempfile, os, json
from api import create_app

# set up flask client and anything else
def set_up():
    file_object, file_location = tempfile.mkstemp()
    test_config = {
        "SECRET_KEY": "testing",
        "DEBUG": False,
        "TESTING": True,
    }
    app = create_app(test_config)
    client = app.test_client()
    with client:
        with app.app_context():
            # any setup goes here
            pass
    return client, file_object

# test our basic hello world route
def test_hello():
    client, file_object = set_up()
    with client:
        response = client.get("/hello")
        assert response.status == 200 or "200 OK"
        assert json.loads(response.get_data(as_text=True)) == {
            "hello": "world",
        }
    os.close(file_object)