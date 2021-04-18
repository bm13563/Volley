from api import create_app


def set_up(additional_config=None, additional_set_up=None):
    app = create_app(additional_config)
    client = app.test_client()
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
