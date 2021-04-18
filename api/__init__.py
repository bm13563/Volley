from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

db = MongoEngine()
login_manager = LoginManager()


def create_app(additional_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # load config files into app.config
    app.config.from_envvar("APP_CONFIG_FILE", silent=True)

    # if additional testing config is passed
    if additional_config is not None:
        [
            app.config.update({key: item})
            for key, item in additional_config.items()
        ]

    # set up our database - to move to a database.py file at some point
    db.init_app(app)

    # set up our login manager. using flask-login for security
    login_manager.init_app(app)

    # import all controllers and register all blueprints
    from .controllers import events, users, authentication

    controllers = [events, users, authentication]
    for c in controllers:
        app.register_blueprint(c.blueprint)

    return app
