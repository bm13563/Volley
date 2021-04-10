from flask import Blueprint, current_app, request, g, jsonify
from flask_login import login_user, logout_user

from .. import login_manager
from ..models.users import User


blueprint = Blueprint('auth', __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(authentication_id):
    user = User.objects.get(authentication__authentication_id=authentication_id)
    return user.authentication


@blueprint.route("/log_in", methods=["POST"])
def log_in():
    """
    Log a user in.
    POST example for postman - https://www.getpostman.com/collections/2fbc6714da799092592b
    """
    args = request.get_json()
    username = args["username"]
    password = args["password"]

    if User.objects(authentication__username=args["username"]):
        user = User.objects.get(authentication__username=args["username"])
        authentication = user.authentication
        
        if authentication.check_password(args["password"]):
            login_user(authentication)
        else:
            return "Incorrect password"

    else:
        return "User does not exist"

    return "Successfully logged in!"
   

@blueprint.route("/log_out", methods=["POST"])
def log_out():
    logout_user()
    return "Successfully logged out!"