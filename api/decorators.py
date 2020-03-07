from flask_jwt_extended import get_jwt_identity
from mongoengine import DoesNotExist
from functools import wraps

from api.database.model import User
from api.errors import InvalidAuthorization


def authentication(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        try:
            User.objects.get(id=user_id)
            return f(*args, **kwargs)
        except DoesNotExist:
            raise InvalidAuthorization
    return decorated_function
