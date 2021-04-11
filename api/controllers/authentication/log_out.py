from flask import g
from flask_login import logout_user


def auth_log_out():
    logout_user()
    del g.user
    return "Successfully logged out!"
