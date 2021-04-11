from flask import request, g
from flask_login import login_user

from ...models.users import User, Metadata, Profile, Authentication


def auth_register():
    """
    Registers a user, adding a new User document to the Users collection.

        Parameters:
                args: A JSON object with the following keys:
                        name (json -> str): The display name of the user.
                        summary (json -> str): A user's submitted summary information, for a profile.
                        interests (json -> array[str]): The volunteering categories that a user is interested in.
                        approximate_location (json -> array[number]): The latitude and longitude of the user.
                        username (json -> str): The username (email) of the user.
                        password (json -> str): The plain-text password of the user.

        Returns:
                confirmation (str): A confirmation that the user has been registered.
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
