from flask import Blueprint, g

from ... import login_manager
from ...models.users import User
from .register import auth_register
from .log_in import auth_log_in
from .log_out import auth_log_out


blueprint = Blueprint("auth", __name__, url_prefix="/auth")


# if this gets more complex, this should have it's own file
@login_manager.user_loader
def load_user(authentication_id):
    user = User.objects.get(
        authentication__authentication_id=authentication_id
    )
    # update the user here, to make sure that we're referencing the most
    # up-to-date user
    g.user = user
    return user.authentication


@blueprint.route("/register", methods=["POST"])
def register():
    return auth_register()


@blueprint.route("/log_in", methods=["POST"])
def log_in():
    return auth_log_in()


@blueprint.route("/log_out", methods=["POST"])
def log_out():
    return auth_log_out()
