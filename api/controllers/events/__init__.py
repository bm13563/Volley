from flask import Blueprint
from flask_login import login_required

from .add import events_add
from .update import events_update


blueprint = Blueprint("events", __name__, url_prefix="/events")


@blueprint.route("/add", methods=["POST"])
@login_required
def add():
    return events_add()


@blueprint.route("/add", methods=["POST"])
@login_required
def update():
    return events_update()
