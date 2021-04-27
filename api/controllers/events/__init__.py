from flask import Blueprint
from flask_login import login_required

from .get import events_get
from .add import events_add
from .update import events_update


blueprint = Blueprint("events", __name__, url_prefix="/events")


@blueprint.route("/get/<event_id>", methods=["POST"])
@login_required
def event(event_id):
    return events_get(event_id)


@blueprint.route("/add", methods=["POST"])
@login_required
def add():
    return events_add()


@blueprint.route("/add", methods=["POST"])
@login_required
def update():
    return events_update()
