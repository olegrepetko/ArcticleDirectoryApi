from bson import ObjectId
from bson.errors import InvalidId
from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError, \
    OperationError

from api.database.model import Category, User
from api.decorators import authentication
from api.errors import CategoryAlreadyExistsError, InternalServerError, UpdatingCategoryError, DeletingCategoryError, \
    CategoryNotExistsError, ArticleRefersCategoryError, InvalidAuthorization


class CategoriesApi(Resource):
    def get(self):
        categories = Category.objects().to_json()
        return Response(categories, mimetype="application/json", status=200)

    @jwt_required
    @authentication
    def post(self):
        try:
            body = request.get_json()
            category = Category(**body)
            category.save()
            return {'id': str(category.id)}, 200
        except (ValidationError, FieldDoesNotExist) as e:
            raise e
        except NotUniqueError:
            raise CategoryAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class CategoryApi(Resource):

    @jwt_required
    @authentication
    def put(self, id):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidId

            body = request.get_json()
            Category.objects.get(id=id).update(**body)
            return '', 200
        except (ValidationError, InvalidId) as e:
            raise e
        except OperationError:
            raise ValidationError
        except InvalidQueryError:
            raise FieldDoesNotExist
        except DoesNotExist:
            raise CategoryNotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    @authentication
    def delete(self, id):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidId

            category = Category.objects.get(id=id)
            category.delete()
            return '', 200
        except InvalidId as e:
            raise e
        except DoesNotExist:
            raise CategoryNotExistsError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidId

            category = Category.objects.get(id=id).to_json()
            return Response(category, mimetype="application/json", status=200)
        except InvalidId as e:
            raise e
        except DoesNotExist:
            raise CategoryNotExistsError
        except Exception:
            raise InternalServerError
