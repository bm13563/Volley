from api import create_app


base_data = {
    "test_id": "60872f44eecdc50c62b0de96",
    "test_date": "202104261000",
    "test_password": "tuneful",
}


def set_up(additional_config=None, additional_set_up=None):
    app = create_app(additional_config)
    client = app.test_client()
    tear_down()
    with client:
        with app.app_context():
            if callable(additional_set_up):
                additional_set_up()
            else:
                pass
    return app, client


def tear_down():
    from api.models.events import Event
    from api.models.users import User

    models = [Event, User]

    for m in models:
        for document in m.objects:
            document.delete()
