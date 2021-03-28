from flask import Blueprint, current_app, request, g, jsonify
from ..models.events_model import Event, Metadata, Status, Setting
from ..utilities.utilities import str_to_date

blueprint = Blueprint('events', __name__, url_prefix="/events")

@blueprint.route("/add", methods=["GET"])
def add():
    """
    Add an event to the Events collection.
    Example GET: "/events/add?category=litter&event_start=202104231600&event_end=202104231800&x_location=-1.756465&y_location=53.453474"
    """
    # parse mandatory arguments
    args = {}
    for argument in ["category", "event_start", "event_end", "x_location", "y_location"]:
        if argument in request.args:
            args[argument] = request.args[argument]
        else:
            return jsonify({"error": f"please supply {argument} for the event"})

    # construct child documents
    status = Status()
    metadata = Metadata(
        category=args["category"]
        )
    setting = Setting(
        event_start=str_to_date(args["event_start"]), 
        event_end=str_to_date(args["event_end"]), 
        location=[float(args["x_location"]), float(args["y_location"])]
        )

    # pack our documents into the parent event document
    event = Event(metadata=metadata, status=status, setting=setting)
    event.validate()
    event.save()
    event_id = str(event.id)
    return {
        event_id: event.metadata.category
    }