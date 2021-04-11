from flask import request, g
from flask_login import login_user

from ...models.users import User, Metadata, Profile, Authentication


def auth_register():
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
    profile = Profile()
    profile.name = args["name"]
    profile.summary = args["summary"]
    profile.interests = args["interests"]
    profile.approximate_location = args["approximate_location"]

    # get authentication, hash password
    authentication = Authentication()
    authentication.username = args["username"]
    authentication.set_password(args["password"])

    # pack embedded documents into the parent user document
    user = User()
    user.metadata = metadata
    user.profile = profile
    user.authentication = authentication

    # validate, upload to database and return
    user.validate()
    user.save()

    # log the user in automatically
    login_user(authentication)
    g.user = user

    return "successfully added user " + str(user.id)
