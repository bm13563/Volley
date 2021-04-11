from flask import request, g

from ...models.events import (
    Event,
    Metadata,
    Status,
    Setting,
    Description,
    Document,
    Parameters,
)
from ...models.users import User
from ...utilities.utilities import str_to_date


def events_add():
    """
    Add an event, adding a new Event document to the Events collection.

        Parameters:
                args: A JSON object with the following keys:
                        category (json -> str): The category of the event.
                        event_start (json -> str): The start time of the event in the form YYYYmmddHHMM.
                        event_end (json -> str): The end time of the event in the form YYYYmmddHHMM.
                        location (json -> array[number]): The latitude and longitude of the event.
                        name (json -> str): The name of the event.
                        summary (json -> str): The summary for the event.
                        social (json -> str): The social for the event.
                        explanations (json -> array[str]): An array containing the explanation for each document.
                        max_attendance (json -> number): The max attendance for the event.

        Returns:
                confirmation (str): A confirmation that the event has been added.
    """
    args = request.get_json()
    user = g.user

    # get status
    status = Status()

    # get metadata
    # owner is the user that is creating the event ie. the user that is
    # currently logged in
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

    # get the documents. the explanation for each document is passed as a list
    # so we need to iterate through them
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

    return "successfully created event " + str(event.id)
