from flask import Blueprint, current_app, request, g, jsonify
from ..models.events_model import Event

blueprint = Blueprint('events', __name__, url_prefix="/events")

@blueprint.route("/add", methods=["GET"])
def add():
    if "name" in request.args:
        name = request.args["name"]
    else:
        return jsonify({"error": "please supply a name for the event"})

    event = Event(name=name)
    event.save()
    event_id = str(event.id)
    return {
        event_id: {
            "name": event.name,
        }
    }