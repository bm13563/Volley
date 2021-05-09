from flask import Blueprint
from flask_login import login_required

from .update import users_update
from .user import users_user


blueprint = Blueprint("users", __name__, url_prefix="/users")


@blueprint.route("/user/<user_id>", methods=["GET"])
@login_required
def user(user_id):
    return users_user(user_id)


@blueprint.route("/update", methods=["POST"])
@login_required
def update():
    return users_update()
