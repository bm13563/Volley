from ...models.users import User
from ...utilities.utilities import make_error


def users_get(user_id):
    try:
        user = User.objects.get(id=user_id).to_json()
        return user
    except User.DoesNotExist:
        return make_error(404, "User does not exist")
