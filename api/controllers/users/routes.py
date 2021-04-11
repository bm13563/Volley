from flask import Blueprint
from flask_login import login_required

from .update import users_update


blueprint = Blueprint('users', __name__, url_prefix="/users")


@blueprint.route("/update", methods=["POST"])
@login_required
def update():
    return users_update()