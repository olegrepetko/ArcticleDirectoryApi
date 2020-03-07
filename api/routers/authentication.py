from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, ValidationError, DoesNotExist

from api.database.model import User
from api.errors import EmailAlreadyExistsError, InternalServerError, UnauthorizedError


class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.generate_password_hash()
            user.save()
            return {'id': str(user.id)}, 200
        except (FieldDoesNotExist, ValidationError) as e:
            raise e
        except ValueError:
            raise ValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError
            access_token = create_access_token(identity=str(user.id))
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
