from datetime import datetime

from .. import db


class Event(db.Document):
    metadata = db.ReferenceField("Meta")


class Meta(db.Document):
    created = db.DateTimeField(default=datetime.now)
    category = db.StringField(max_length=50)

