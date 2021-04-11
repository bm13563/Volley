from flask import request, g


def users_update():
    """
    Updates a User's information.

        Parameters:
                args: A JSON object with the following keys:
                        name (str), optional: The display name of the user.
                        summary (str), optional: A user's submitted summary information, for a profile.
                        interests (array[str]), optional: The volunteering categories that a user is interested in.
                        approximate_location (array[number]), optional: The latitude and longitude of the user.
                        username (str), optional: The username (email) of the user.
                        password (str), optional: The plain-text password of the user.

        Returns:
                confirmation (str): A confirmation that the user has been registered.
    """
    args = request.get_json()
    user = g.user

    # update profile information, if key doesnt exist in args, use existing
    # value
    user.profile.name = args.get("name", user.profile.name)
    user.profile.summary = args.get("summary", user.profile.summary)
    user.profile.interests = args.get("interests", user.profile.interests)
    user.profile.approximate_location = args.get(
        "approximate_location", user.profile.approximate_location
    )

    # update profile information, if key doesnt exist in args, use existing
    # value
    user.authentication.username = args.get(
        "username", user.authentication.username
    )

    # because password is encrypted, we don't want to replace with the
    # existing value
    if "password" in args:
        user.authentication.set_password(args["password"])

    # validate, upload to database and return
    user.validate()
    user.save()
    return "successfully updated for user " + str(user.id)
