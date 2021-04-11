from flask import request, g, jsonify
from flask_login import login_user

from ...models.users import User


def auth_log_in():
    """
    Log a user in.
    POST example for postman - https://www.getpostman.com/collections/2fbc6714da799092592b
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