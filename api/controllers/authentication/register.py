from flask import request, g
from flask_login import login_user

from ...models.users import User, Metadata, Profile, Authentication
from ...utilities.utilities import init_model, json_matches_schema, make_error
from .types import register_schema


def auth_register():
    """
    Registers a user, adding a new User document to the Users collection.

        Parameters:
                args (object): A JSON object that adheres to the register_schema type.

        Returns:
                confirmation (str): A confirmation that the user has been registered.
    """
    args = request.get_json()

    # check if we're testing, split out test arguments if we are
    test_args = args.get("test_args", False)
    args.pop("test_args", None)

    # ensure that the input json matches the schema
    schema_match, message = json_matches_schema(args, register_schema)
    if not schema_match:
        return make_error(422, message)

    # check if the username already exists
    if User.objects(
        authentication__username=args["authentication"]["username"]
    ):
        return make_error(
            409, "An account already exists with this username, sorry"
        )

    # get metadata
    metadata = init_model(Metadata, test_args)

    # get profile - profile will probably be added after authentication, so may be moved?
    profile = init_model(Profile, test_args)
    profile.name = args["profile"]["name"]
    profile.summary = args["profile"]["summary"]
    profile.interests = args["profile"]["interests"]
    profile.approximate_location = args["profile"]["location"]["coordinates"]

    # get authentication, hash password
    authentication = init_model(Authentication, test_args)
    authentication.username = args["authentication"]["username"]
    authentication.set_password(args["authentication"]["password"])

    # pack embedded documents into the parent user document
    user = init_model(User, test_args)
    user.metadata = metadata
    user.profile = profile
    user.authentication = authentication

    # validate, upload to database and return
    user.validate()
    user.save()

    # log the user in automatically
    login_user(authentication)
    g.user = user

    return user.to_json()
