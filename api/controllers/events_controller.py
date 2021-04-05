from flask import Blueprint, current_app, request, g, jsonify
from ..models.events_model import Event, Metadata, Status, Setting, Description, Document, Parameters
from ..models.users_model import User
from ..utilities.utilities import str_to_date

import pprint


blueprint = Blueprint('events', __name__, url_prefix="/events")


@blueprint.route("/add", methods=["POST"])
def add():
    """
    Add an event to the Events collection.
    POST example for postman - https://www.getpostman.com/collections/2fbc6714da799092592b
    """
    args = request.get_json()

    # get status
    status = Status()

    # get metadata
    owner = User.objects.get(id=args["user_id"])
    metadata = Metadata(
        category=args["category"],
        # embed the document of the user that created the collection as a reference
        owner=owner,
    )

    # get the setting
    setting = Setting(
        event_start=str_to_date(args["event_start"]), 
        event_end=str_to_date(args["event_end"]), 
        location=args["location"],
    )

    # get the description
    description = Description(
        name=args["name"],
        summary=args["summary"],
        social=args["social"],
    )

    # get the documents. the explanation for each document is passed as a list so we need to iterate through them
    documents = []
    for explanation in args["explanations"]:
        document = Document(
            explanation=explanation,
        )
        documents.append(document)

    # get the parameters
    parameters = Parameters(
        max_attendance=args["max_attendance"],
        documents=documents,
    )

    # pack embedded documents into the parent event document
    event = Event(
        metadata=metadata, 
        status=status, 
        setting=setting,
        description=description,
        parameters=parameters,
    )

    # validate, upload to database and return
    event.validate()
    event.save()

    # add the event to the owner's document
    owner.make_event_owner(event.id)
    owner.validate()
    owner.save()

    event_id = str(event.id)
    return {
        event_id: event.metadata.category
    }