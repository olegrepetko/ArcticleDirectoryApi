from .article import ArticlesApi, ArticleApi
from .authentication import SignupApi, LoginApi
from .category import CategoriesApi,CategoryApi


def initialize_routers(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(CategoriesApi, '/api/categories')
    api.add_resource(CategoryApi, '/api/category/<id>')

    api.add_resource(ArticlesApi, '/api/articles')
    api.add_resource(ArticleApi, '/api/article/<id>')
