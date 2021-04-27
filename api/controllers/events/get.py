from ...models.events import Event


def events_get(event_id):
    return Event.objects.get(id=event_id).to_json()
