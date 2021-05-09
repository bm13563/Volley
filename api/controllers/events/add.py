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
from ...utilities.utilities import (
    str_to_date,
    init_model,
    json_matches_schema,
    make_error,
)
from .schemas.events_add_schema import add_schema


def events_add():
    """
    Add an event, adding a new Event document to the Events collection.

        Parameters:
                args (object): A JSON object that adheres to the events_add_schema type.

        Returns:
                confirmation (str): A confirmation that the event has been added.
    """
    args = request.get_json()
    user = g.user

    # check if we're testing, split out test arguments if we are
    test_args = args.get("test_args", False)
    args.pop("test_args", None)

    # ensure that the input json matches the schema
    schema_match, message = json_matches_schema(args, add_schema)
    if not schema_match:
        return make_error(422, message)

    # TODO we'll also need to do a test here that the documents match their schema

    # get status
    status = init_model(Status, test_args)

    # get metadata
    # owner is the user that is creating the event ie. the user that is
    # currently logged in
    owner = User.objects.get(id=str(user.id))
    metadata = init_model(Metadata, test_args)
    metadata.category = args["metadata"]["category"]
    metadata.owner = owner

    # get the setting
    setting = init_model(Setting, test_args)
    setting.event_start = str_to_date(args["setting"]["event_start"])
    setting.event_end = str_to_date(args["setting"]["event_end"])
    setting.location = args["setting"]["location"]

    # get the description
    description = init_model(Description, test_args)
    description.name = args["description"]["name"]
    description.summary = args["description"]["summary"]
    description.social = args["description"]["social"]

    # get the documents. the explanation for each document is passed as a list
    # so we need to iterate through them
    documents = []
    for input_document in args["parameters"]["documents"]:
        document = init_model(Document, test_args)
        document.explanation = input_document
        documents.append(document)

    # get the parameters
    parameters = init_model(Parameters, test_args)
    parameters.max_attendance = args["parameters"]["max_attendance"]
    parameters.documents = documents

    # pack embedded documents into the parent event document
    event = init_model(Event, test_args)
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

    return event.to_json()
