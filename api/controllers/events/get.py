from ...models.events import Event
from ...utilities.utilities import make_error


def events_get(event_id):
    try:
        event = Event.objects.get(id=event_id).to_json()
        return event
    except Event.DoesNotExist:
        return make_error(404, "Event does not exist")
