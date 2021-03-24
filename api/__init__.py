import os
from flask import Flask, g


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_envvar("APP_CONFIG_FILE", silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route("/hello")
    def hello():
        return {
            "hello": "world",
        }

    return app