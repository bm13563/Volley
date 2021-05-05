import types
from datetime import datetime
from bson.objectid import ObjectId
from jsonschema import validate


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
    def getshape(d):
        if isinstance(d, dict):
            return {k: getshape(d[k]) for k in d if k != "type"}
        else:
            return {}

    json_shape = getshape(json)
    schema_shape = getshape(schema["properties"])
    if json_shape == schema_shape:
        try:
            validate(instance=json, schema=schema)
        except Exception as e:
            print(e)
            return {"error": "Input JSON types do not match that of schema"}
    else:
        print(json_shape)
        print(schema_shape)
        return {"error": "Input JSON does not match shape/ keys of schema"}

    return {}
