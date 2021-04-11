from flask import request, g, jsonify

from ...models.events import Event, Metadata, Status, Setting, Description, Document, Parameters
from ...models.users import User
from ...utilities.utilities import str_to_date


def events_add():
    """
    Add an event to the Events collection.
    POST example for postman - https://www.getpostman.com/collections/2fbc6714da799092592b
    """
    args = request.get_json()
    user = g.user

    # get status
    status = Status()

    # get metadata
    # owner is the user that is creating the event ie. the user that is currently logged in
    owner = User.objects.get(id=str(user.id))
    metadata = Metadata()
    metadata.category = args["category"]
    metadata.owner = owner

    # get the setting
    setting = Setting()
    setting.event_start = str_to_date(args["event_start"])
    setting.event_end = str_to_date(args["event_end"])
    setting.location = args["location"]
    
    # get the description
    description = Description()
    description.name = args["name"]
    description.summary = args["summary"]
    description.social = args["social"]

    # get the documents. the explanation for each document is passed as a list so we need to iterate through them
    documents = []
    for explanation in args["explanations"]:
        document = Document()
        document.explanation = explanation
        documents.append(document)

    # get the parameters
    parameters = Parameters()
    parameters.max_attendance = args["max_attendance"]
    parameters.documents = documents

    # pack embedded documents into the parent event document
    event = Event()
    event.metadata = metadata
    event.status = status
    event.setting = setting
    event.description = description
    event.parameters = parameters

    # validate, upload to database and return
    event.validate()
    event.save()

    # add the event to the owner's document
    owner.make_event_owner(event.id)
    owner.validate()
    owner.save()

    event_id = str(event.id)
    return "successfully created event " + str(event.id)