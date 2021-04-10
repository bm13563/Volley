from datetime import datetime
from bson.objectid import ObjectId

from .. import db


class Metadata(db.EmbeddedDocument):
    metadata_id = db.ObjectIdField(default=lambda: ObjectId())
    created = db.DateTimeField(default=datetime.now)
    owner = db.ReferenceField('User')
    category = db.StringField(max_length=50, required=True) # this should be an enum eventually
    # chat = ReferenceField


class Status(db.EmbeddedDocument):
    status_id = db.ObjectIdField(default=lambda: ObjectId())
    finished = db.BooleanField(default=False)
    ongoing = db.BooleanField(default=False)
    full = db.BooleanField(default=False)
    cancelled = db.BooleanField(default=False)


class Setting(db.EmbeddedDocument):
    setting_id = db.ObjectIdField(default=lambda: ObjectId())
    event_start = db.DateTimeField(required=True)
    event_end = db.DateTimeField(required=True)
    location = db.PointField(max_length=2, required=True)


class Description(db.EmbeddedDocument):
    description_id = db.ObjectIdField(default=lambda: ObjectId())
    name = db.StringField(max_length=50, required=True)
    summary = db.StringField(max_length=200, required=True)
    social = db.StringField(max_length=50, required=True)
    # picture = UrlField


class Document(db.EmbeddedDocument):
    document_id = db.ObjectIdField(default=lambda: ObjectId())
    explanation = db.StringField(max_length=200, required=True)
    # example = UrlField


class Parameters(db.EmbeddedDocument):
    paramaters_id = db.ObjectIdField(default=lambda: ObjectId())
    max_attendance = db.IntField(required=True)
    approval_required = db.BooleanField(default=False)
    documents_required = db.BooleanField(default=False)
    documents = db.ListField(db.EmbeddedDocumentField(Document))


class Attendee(db.EmbeddedDocument):
    attendee_id = db.ObjectIdField(default=lambda: ObjectId())
    user = db.ReferenceField("User")
    attended = db.BooleanField(default=False)
    documents = db.ListField(db.EmbeddedDocumentField(Document))


class Requests(db.EmbeddedDocument):
    requests_id = db.ObjectIdField(default=lambda: ObjectId())
    current_requests = db.IntField(default=0)
    attendees = db.ListField(db.EmbeddedDocumentField(Attendee))


class Attendance(db.EmbeddedDocument):
    _id = db.ObjectIdField(default=lambda: ObjectId())
    current_attendance = db.IntField(default=0)
    attendees = db.ListField(db.EmbeddedDocumentField(Attendee))


class Event(db.Document):
    metadata = db.EmbeddedDocumentField(Metadata)
    status = db.EmbeddedDocumentField(Status)
    setting = db.EmbeddedDocumentField(Setting)
    description = db.EmbeddedDocumentField(Description)
    parameters = db.EmbeddedDocumentField(Parameters)

