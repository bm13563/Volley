from flask import Blueprint, current_app, request, g, jsonify
from flask_login import login_user, logout_user

from .. import login_manager
from ..models.users import User, Metadata, Profile, Authentication


blueprint = Blueprint('auth', __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(authentication_id):
    # authentication_id = "607235f2418964fab72d8142"
    user = User.objects.get(authentication__authentication_id=authentication_id)
    # update the user here, to make sure that we're referencing the most up-to-date user
    g.user = user
    return user.authentication


# does this want to be auth/register?
@blueprint.route("/register", methods=["POST"])
def register():
    """
    Add a user to the Users collection. Requires their profile information too.
    POST example for postman - https://www.getpostman.com/collections/2fbc6714da799092592b
    """
    args = request.get_json()

    # check if the username already exists
    if User.objects(authentication__username=args["username"]):
        return "An account already exists with this username, sorry"

    # get metadata
    metadata = Metadata()

    # get profile - profile will probably be added after authentication, so may be moved?
    profile = Profile(
        name=args["name"],
        summary=args["summary"],
        interests=args["interests"],
        approximate_location=args["approximate_location"],
    )

    # get authentication, hash password
    authentication = Authentication(
        username=args["username"],
    )
    authentication.set_password(args["password"])

    # pack embedded documents into the parent user document
    user = User(
        metadata=metadata,
        profile=profile,
        authentication=authentication,
    )

    # validate, upload to database and return
    user.validate()
    user.save()
    user_id = str(user.id)

    # log the user in automatically
    login_user(authentication)

    return "successfully added user " + str(user.id)


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
            g.user = user
        else:
            return "Incorrect password"
    else:
        return "User does not exist"

    return "Successfully logged in!"
   

@blueprint.route("/log_out", methods=["POST"])
def log_out():
    logout_user()
    del g.user
    return "Successfully logged out!"