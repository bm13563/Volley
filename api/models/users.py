from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db
from ..utilities.utilities import generate_id


class Metadata(db.EmbeddedDocument):
    id = db.ObjectIdField(primary_key=True, default=generate_id())
    created = db.DateTimeField(default=datetime.now)


class Profile(db.EmbeddedDocument):
    id = db.ObjectIdField(primary_key=True, default=generate_id())
    name = db.StringField(max_length=50, required=True)
    summary = db.StringField(max_length=200, required=True)
    # picture = UrlField
    interests = db.ListField(db.StringField(max_length=50))
    score = db.IntField(default=0)
    approximate_location = db.PointField(max_length=2, required=True)


class Authentication(db.EmbeddedDocument):
    # username will be an email. will need to verify
    id = db.ObjectIdField(primary_key=True, default=generate_id())
    username = db.StringField(max_length=100, required=True)
    password_hash = db.StringField()
    verified = db.BooleanField(default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class User(db.Document):
    id = db.ObjectIdField(primary_key=True, default=generate_id())
    metadata = db.EmbeddedDocumentField("Metadata")
    profile = db.EmbeddedDocumentField("Profile")
    authentication = db.EmbeddedDocumentField("Authentication")
    events = db.ListField(db.ReferenceField("Event"))

    # makes this user the owner of an event
    def make_event_owner(self, event_id):
        from ..models.events import Event

        self.events.append(Event.objects.get(id=event_id))
