import os
from flask import Flask, g
from flask_mongoengine import *


db = MongoEngine()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_envvar("APP_CONFIG_FILE", silent=True)
    else:
        app.config.from_mapping(test_config)

    # set up our database - to move to a database.py file at some point
    db.init_app(app)

    # import all controllers and register all blueprints
    from .controllers import events_controller
    controllers = [events_controller]
    for controller in controllers:
        app.register_blueprint(controller.blueprint)

    return app