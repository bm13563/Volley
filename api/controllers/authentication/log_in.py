from flask import request, g
from flask_login import login_user

from ...models.users import User


def auth_log_in():
    """
    Log a user in.

        Parameters:
                args: A JSON object with the following keys:
                        username (str): The username of the user.
                        password (str): The plain-text password of the user.

        Returns:
                confirmation (str): A confirmation that the user has been logged in.
    """
    args = request.get_json()

    if not User.objects(authentication__username=args["username"]):
        return "User does not exist"

    user = User.objects.get(authentication__username=args["username"])
    authentication = user.authentication

    if authentication.check_password(args["password"]):
        login_user(authentication)
        g.user = user
    else:
        return "Incorrect password"

    return "Successfully logged in!"
