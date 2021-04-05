from datetime import datetime

from .. import db


class Metadata(db.EmbeddedDocument):
    created = db.DateTimeField(default=datetime.now)
    owner = db.ReferenceField('User')
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
    location = db.PointField(max_length=2, required=True)


class Description(db.EmbeddedDocument):
    name = db.StringField(max_length=50, required=True)
    summary = db.StringField(max_length=200, required=True)
    social = db.StringField(max_length=50, required=True)
    # picture = UrlField


class Document(db.EmbeddedDocument):
    explanation = db.StringField(max_length=200, required=True)
    # example = UrlField


class Parameters(db.EmbeddedDocument):
    max_attendance = db.IntField(required=True)
    approval_required = db.BooleanField(default=False)
    documents_required = db.BooleanField(default=False)
    documents = db.ListField(db.EmbeddedDocumentField(Document))


class Attendee(db.EmbeddedDocument):
    user = db.ReferenceField("User")
    attended = db.BooleanField(default=False)
    documents = db.ListField(db.EmbeddedDocumentField(Document))


class Requests(db.EmbeddedDocument):
    current_requests = db.IntField(default=0)
    attendees = db.ListField(db.EmbeddedDocumentField(Attendee))


class Attendance(db.EmbeddedDocument):
    current_attendance = db.IntField(default=0)
    attendees = db.ListField(db.EmbeddedDocumentField(Attendee))


class Event(db.Document):
    metadata = db.EmbeddedDocumentField(Metadata)
    status = db.EmbeddedDocumentField(Status)
    setting = db.EmbeddedDocumentField(Setting)
    description = db.EmbeddedDocumentField(Description)
    parameters = db.EmbeddedDocumentField(Parameters)

