from flask import Blueprint, current_app, request, g, jsonify
from ..models.events_model import Event, Meta

blueprint = Blueprint('events', __name__, url_prefix="/events")

@blueprint.route("/add", methods=["GET"])
def add():
    if "category" in request.args:
        category = request.args["category"]
    else:
        return jsonify({"error": "please supply a category for the event"})

    meta = Meta(category=category)
    meta.save()
    event = Event(metadata=meta)
    event.save()
    event_id = str(event.id)
    return {
        event_id: event.metadata.category
    }