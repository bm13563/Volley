import os
from flask import Flask, g
from flask_login import LoginManager
from flask_mongoengine import *


db = MongoEngine()
login_manager = LoginManager()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_envvar("APP_CONFIG_FILE", silent=True)
    else:
        app.config.from_mapping(test_config)

    # set up our database - to move to a database.py file at some point
    db.init_app(app)

    # set up our login manager. using flask-login for security
    login_manager.init_app(app)

    # import all controllers and register all blueprints
    from .controllers import events, users, authentication
    controllers = [events, users, authentication]
    for c in controllers:
        app.register_blueprint(c.routes.blueprint)

    return app