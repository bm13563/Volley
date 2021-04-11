from flask import g
from flask_login import logout_user


def auth_log_out():
    """
    Logs a User out.

            Returns:
                confirmation (str): A confirmation that the user has been logged out.
    """
    logout_user()
    del g.user
    return "Successfully logged out!"
