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
        pass

    def check_password(self, password):
        print(self.password_hash, password)
        return self.password_hash == password

    if test_args:
        model.set_password = types.MethodType(set_password, model_object)
        model.check_password = types.MethodType(check_password, model_object)
        for field_name, field_type in model._fields.items():
            if "ObjectIdField" in str(field_type):
                setattr(model_object, field_name, test_args["test_id"])
            # TODO exception for incorrect format
            if "DateTimeField" in str(field_type):
                setattr(
                    model_object,
                    field_name,
                    datetime.strptime(test_args["test_date"], "%Y%m%d%H%M"),
                )
            if "password" in str(field_name).lower():
                setattr(model_object, field_name, test_args["test_password"])
    return model_object
