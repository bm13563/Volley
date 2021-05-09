from flask import request, g
from flask_login import login_user

from ...models.users import User
from ...utilities.utilities import json_matches_schema, make_error
from .schemas.authentication_log_in_schema import log_in_schema


def auth_log_in():
    """
    Log a user in.

        Parameters:
                args (object): A JSON object that adheres to the log_in_schema type.

        Returns:
                confirmation (str): A confirmation that the user has been logged in.
    """
    args = request.get_json()

    # check if we're testing, split out test arguments if we are
    args.pop("test_args", None)

    # ensure that the input json matches the schema
    schema_match, message = json_matches_schema(args, log_in_schema)
    if not schema_match:
        return make_error(422, message)

    if not User.objects(
        authentication__username=args["authentication"]["username"]
    ):
        return make_error(404, "User does not exist")

    user = User.objects.get(
        authentication__username=args["authentication"]["username"]
    )
    authentication = user.authentication

    if authentication.check_password(args["authentication"]["password"]):
        login_user(authentication)
        g.user = user
    else:
        return make_error(403, "Incorrect password")

    return user.to_json()
