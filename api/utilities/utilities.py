from flask import jsonify
import types
from datetime import datetime
from bson.objectid import ObjectId


def str_to_date(date_time_str):
    return datetime.strptime(date_time_str, "%Y%m%d%H%M")


def generate_id():
    return ObjectId()


def init_model(model, test_args=False):
    model_object = model()

    def set_password(self, password):
        self.password_hash = password

    def check_password(self, password):
        return self.password_hash == password

    if test_args:
        model.set_password = types.MethodType(set_password, model_object)
        model.check_password = types.MethodType(check_password, model_object)
        for field_name, field_type in model._fields.items():
            if "ObjectIdField" in str(field_type):
                setattr(model_object, field_name, test_args["test_id"])
            if "DateTimeField" in str(field_type):
                setattr(
                    model_object,
                    field_name,
                    datetime.strptime(test_args["test_date"], "%Y%m%d%H%M"),
                )
    return model_object


def json_matches_schema(json, schema):
    def getjson(d):
        if isinstance(d, dict):
            return {k: getjson(d[k]) for k in d}
        else:
            return str(type(d).__name__)

    def getschema(d):
        if isinstance(d, dict):
            return {k: getschema(d[k]) for k in d}
        else:
            return str(d.__name__)

    if getjson(json) == getschema(schema):
        return {}
    else:
        print(getjson(json))
        print(getschema(schema))
        return {"error": "Input JSON does not match shape/ types of schema"}


def make_error(status_code, message):
    response = jsonify(
        {
            "status": status_code,
            "message": message,
        }
    )
    response.status_code = status_code
    return response
