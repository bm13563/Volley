from ...models.events import Event


def events_event(event_id):
    try:
        event = Event.objects.get(id=event_id).to_json()
        return event
    except Event.DoesNotExist:
        return "This event does not exist"
