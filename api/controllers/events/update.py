from flask import request

from ...models.events import Event


# this method is not done yet
def events_update():
    """
    Update an Event's information.

        Parameters:
                args (object): A JSON object that adheres to the events_update type.

        Returns:
                confirmation (str): A confirmation that the event has been updated.
    """
    args = request.get_json()

    event = Event.objects.get(id=args["event_id"])

    # update metadata
    event.metadata.category = args.get("category", event.metadata.category)

    # update setting
    event.setting.event_start = args.get(
        "event_start", event.setting.event_start
    )
    event.setting.event_end = args.get("event_end", event.setting.event_end)
    event.setting.location = args.get("location", event.setting.location)

    # update the description
    event.description.name = args.get("name", event.description.name)
    event.description.summary = args.get("summary", event.description.summary)
    event.description.social = args.get("social", event.description.social)

    # update the documents
    # TODO

    # get the parameters
    event.parameters.max_attendance = args.get("max_attendance")

    # validate, upload to database and return
    event.validate()
    event.save()

    return event.to_json()
