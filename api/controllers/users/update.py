from flask import request, g

from ...utilities.utilities import json_matches_schema, make_error
from .types import update_schema


def users_update():
    """
    Updates a User's information.

        Parameters:
                args: test

        Returns:
                confirmation (str): test
    """
    args = request.get_json()
    user = g.user

    # check if we're testing, split out test arguments if we are
    args.get("test_args", False)
    args.pop("test_args", None)

    # ensure that the input json matches the schema
    schema_match, message = json_matches_schema(args, update_schema)
    if not schema_match:
        return make_error(422, message)

    # update profile information, if key doesnt exist in args, use existing
    # value
    user.profile.name = args["profile"]["name"]
    user.profile.summary = args["profile"]["summary"]
    user.profile.interests = args["profile"]["interests"]
    user.profile.approximate_location = args["profile"]["location"][
        "coordinates"
    ]

    # update profile information, if key doesnt exist in args, use existing
    # value
    user.authentication.username = args["authentication"]["username"]

    # because password is encrypted, we don't want to replace with the
    # existing value
    if "password" in args:
        user.authentication.set_password(args["password"])

    # validate, upload to database and return
    user.validate()
    user.save()
    return user.to_json()
