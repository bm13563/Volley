from flask import request, g


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
    return user.to_json()
