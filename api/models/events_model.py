from bson.objectid import ObjectId

from .. import db


class Event(db.Document):
    name = db.StringField(max_length=50)



