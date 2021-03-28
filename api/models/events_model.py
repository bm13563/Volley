from datetime import datetime

from .. import db


class Metadata(db.EmbeddedDocument):
    created = db.DateTimeField(default=datetime.now)
    # owner = ReferenceField
    category = db.StringField(max_length=50, required=True) # this should be an enum eventually
    # chat = ReferenceField


class Status(db.EmbeddedDocument):
    finished = db.BooleanField(default=False)
    ongoing = db.BooleanField(default=False)
    full = db.BooleanField(default=False)
    cancelled = db.BooleanField(default=False)


class Setting(db.EmbeddedDocument):
    event_start = db.DateTimeField(required=True)
    event_end = db.DateTimeField(required=True)
    location = db.PointField(required=True, max_length=2)


class Description(db.EmbeddedDocument):
    name = db.StringField(max_length=50)
    summary = db.StringField(max_length=200)
    social = db.StringField(max_length=50)
    # picture = UrlField


class Event(db.Document):
    metadata = db.EmbeddedDocumentField(Metadata)
    status = db.EmbeddedDocumentField(Status)
    setting = db.EmbeddedDocumentField(Setting)

