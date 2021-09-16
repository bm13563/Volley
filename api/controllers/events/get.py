from flask import g

from ...models.events import Event
from ...utilities.utilities import make_error


# think we'll need 3 views:
# 1. owner view
# 2. attendee view
# 3. non-attendee view
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
