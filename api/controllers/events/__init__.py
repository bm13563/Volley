from flask import Blueprint
from flask_login import login_required

from .event import events_event
from .add import events_add
from .update import events_update


blueprint = Blueprint("events", __name__, url_prefix="/events")


@blueprint.route("/event/<event_id>", methods=["GET"])
@login_required
def event(event_id):
    return events_event(event_id)


@blueprint.route("/add", methods=["POST"])
@login_required
def add():
    return events_add()


@blueprint.route("/update", methods=["POST"])
@login_required
def update():
    return events_update()
