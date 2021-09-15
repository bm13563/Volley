from flask import request, g

from api.utilities.utilities import init_model, json_matches_schema, make_error
from ...models.events import Attendee, Event
from .types import events_register_schema


def events_register():
    """
    Registers the logged-in user to an event

        Parameters:
                args (object): A JSON object that adheres to the events_register_schema type.

        Returns:
                confirmation (str): A confirmation that the event has been updated.
    """
    args = request.get_json()

    test_args = args.get("test_args", False)
    args.pop("test_args", None)

    # ensure that the input json matches the schema
    schema_match, message = json_matches_schema(args, events_register_schema)
    if not schema_match:
        return make_error(422, message)

    event = Event.objects.get(id=args["event_id"])
    current_attendance = len(event.parameters.attendance.attendees)

    if current_attendance >= event.parameters.max_attendance:
        return make_error(400, "Sorry, this event is full")

    if event.is_user_attending(g.user):
        return make_error(400, "You are already signed up to this event")

    if g.user == event.metadata.owner:
        return make_error(400, "You can't sign up to your own event")

    attendee = init_model(Attendee, test_args)
    attendee.user = g.user
    attendee.attended = False
    attendee.documents = []
    event.parameters.attendance.current_attendance += 1
    event.parameters.attendance.attendees.append(attendee)

    event.validate()
    event.save()

    return event.to_json()
