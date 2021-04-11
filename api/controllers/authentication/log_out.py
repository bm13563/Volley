from flask import request, g, jsonify
from flask_login import logout_user

from ...models.users import User


def auth_log_out():
    logout_user()
    del g.user
    return "Successfully logged out!"