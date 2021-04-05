from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db


class Metadata(db.EmbeddedDocument):
    created = db.DateTimeField(default=datetime.now)


class Profile(db.EmbeddedDocument):
    name = db.StringField(max_length=50, required=True)
    summary = db.StringField(max_length=200, required=True)
    # picture = UrlField
    interests = db.ListField()
    score = db.IntField(default=0)
    approximate_location = db.PointField(max_length=2, required=True)


class Authentication(db.EmbeddedDocument):
    # username will be an email. will need to verify
    username = db.StringField(max_length=100, required=True)
    password_hash = db.StringField()
    verified = db.BooleanField(default=False)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
     
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


class User(db.Document):
    metadata = db.EmbeddedDocumentField(Metadata)
    profile = db.EmbeddedDocumentField(Profile)
    authentication = db.EmbeddedDocumentField(Authentication)
    # events = db.EmbeddedDocumentField()