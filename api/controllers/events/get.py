from flask import g

from ...models.events import Event
from ...utilities.utilities import make_error


# will need to check if the user is registered to the event -  if not,
# the user will need to register - if so, they can view the event
def events_get(event_id):
    try:
        event = Event.objects.get(id=event_id)

        if g.user != event.metadata.owner and not event.is_user_attending(
            g.user
        ):
            return make_error(
                403, "You do not have permission to view this event"
            )

        return event.to_json()
    except Event.DoesNotExist:
        return make_error(404, "Event does not exist")
