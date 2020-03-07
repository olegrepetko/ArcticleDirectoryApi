from datetime import datetime

from bson import ObjectId
from bson.errors import InvalidId
from flask_restful import Resource, reqparse
from flask import Response, request
from api.database.model import Category, User, Article
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from api.decorators import authentication
from api.errors import ArticleAlreadyExistsError, InternalServerError, UpdatingArticleError, DeletingArticleError, \
    CategoryNotExistsError, ArticleNotExistsError, CreateOrModifyDateNotCanBeSet, InvalidAuthorization


class ArticlesApi(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category', type=str)
        args = parser.parse_args()

        if args['category'] is not None:
            try:
                category_id = Category.objects(name=args['category']).get()
            except DoesNotExist:
                raise CategoryNotExistsError
            articles = Article.objects(categories=category_id).to_json()
        else:
            articles = Article.objects().to_json()
        return Response(articles, mimetype="application/json", status=200)

    @jwt_required
    @authentication
    def post(self):
        try:
            user_id = get_jwt_identity()
            user = User.objects.get(id=user_id)
            body = request.get_json()

            if 'create_datetime' in body or 'modify_datetime' in body:
                raise CreateOrModifyDateNotCanBeSet
            body['create_datetime'] = None
            body['modify_datetime'] = None

            if 'categories' not in body:
                raise ValidationError
            try:
                body['categories'] = [Category.objects(name=name).get() for name in set(body['categories'])]
            except DoesNotExist:
                raise CategoryNotExistsError

            article = Article(**body, added_by=user)
            article.save()
            return {'id': str(article.id)}, 200

        except (ValidationError, FieldDoesNotExist, CreateOrModifyDateNotCanBeSet, CategoryNotExistsError) as e:
            raise e
        except NotUniqueError:
            raise ArticleAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class ArticleApi(Resource):

    @jwt_required
    @authentication
    def put(self, id):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidId

            body = request.get_json()
            if len(body) == 0:
                raise ValidationError

            if 'create_datetime' in body or 'modify_datetime' in body:
                raise CreateOrModifyDateNotCanBeSet
            body['modify_datetime'] = datetime.utcnow()

            if 'categories' in body:
                try:
                    body['categories'] = [Category.objects(name=name).get() for name in set(body['categories'])]
                except DoesNotExist:
                    raise CategoryNotExistsError

            Article.objects.get(id=id).update(**body)
            return '', 200
        except (InvalidId, CategoryNotExistsError, ValidationError) as e:
            raise e
        except InvalidQueryError:
            raise FieldDoesNotExist
        except DoesNotExist:
            raise ArticleNotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    @authentication
    def delete(self, id):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidId

            user_id = get_jwt_identity()

            article = Article.objects.get(id=id, added_by=user_id)
            article.delete()
            return '', 200
        except InvalidId as e:
            raise e
        except DoesNotExist:
            raise ArticleNotExistsError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidId

            articles = Article.objects.get(id=id).to_json()
            return Response(articles, mimetype="application/json", status=200)
        except InvalidId as e:
            raise e
        except DoesNotExist:
            raise ArticleNotExistsError
        except Exception:
            raise InternalServerError
