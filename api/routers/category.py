from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError, \
    OperationError

from api.database.model import Category
from api.decorators import authentication, validate_id
from api.errors import CategoryAlreadyExistsError, InternalServerError, CategoryNotExistsError, \
    ArticleRefersCategoryError


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
    @validate_id
    def put(self, id):
        try:
            body = request.get_json()
            Category.objects.get(id=id).update(**body)
            return '', 200
        except ValidationError as e:
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
    @validate_id
    def delete(self, id):
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return '', 200
        except OperationError:
            raise ArticleRefersCategoryError
        except DoesNotExist:
            raise CategoryNotExistsError
        except Exception:
            raise InternalServerError

    @validate_id
    def get(self, id):
        try:
            category = Category.objects.get(id=id).to_json()
            return Response(category, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CategoryNotExistsError
        except Exception:
            raise InternalServerError
