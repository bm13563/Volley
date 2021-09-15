from flask import Blueprint
from flask_login import login_required

from .get import events_get
from .add import events_add
from .update import events_update
from .register import events_register


blueprint = Blueprint("events", __name__, url_prefix="/events")


@blueprint.route("/event/<event_id>", methods=["GET"])
@login_required
def get(event_id):
    return events_get(event_id)


@blueprint.route("/add", methods=["POST"])
@login_required
def add():
    return events_add()


@blueprint.route("/update", methods=["POST"])
@login_required
def update():
    return events_update()


@blueprint.route("/register", methods=["POST"])
@login_required
def register():
    return events_register()
