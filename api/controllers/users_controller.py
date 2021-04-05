from flask import Blueprint, current_app, request, g, jsonify
from ..models.users_model import User, Metadata, Profile, Authentication

import pprint

blueprint = Blueprint('users', __name__, url_prefix="/users")

@blueprint.route("/add", methods=["POST"])
def add():
    """
    Add a user to the Users collection.
    POST example for postman - 
    """
    args = request.get_json()

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
    return {
        user_id: "successfully added!"
    }

    